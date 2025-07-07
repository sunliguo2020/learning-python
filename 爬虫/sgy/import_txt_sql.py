# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2025/7/3 14:08
优化版数据导入脚本 - 内存安全版本
特点：
1. 使用服务器端游标避免客户端内存爆炸
2. 分批处理数据减少内存压力
3. 增强错误处理和日志记录
4. 自动重试机制
"""
import logging
import os
import sys
import time
from datetime import datetime

import MySQLdb
from MySQLdb.cursors import SSCursor

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout),
              logging.FileHandler('data_import.log')]
)
logger = logging.getLogger(__name__)


# 配置参数
class Config:
    BATCH_SIZE = 500  # 每批处理文件数
    COMMIT_INTERVAL = 100  # 每多少条提交一次
    MAX_RETRIES = 3  # 最大重试次数
    RETRY_DELAY = 10  # 重试延迟(秒)
    DB_TIMEOUT = 30  # 数据库操作超时(秒)


# 创建数据库连接
def create_db_connection():
    """创建数据库连接 使用服务器游标"""
    try:
        conn = MySQLdb.connect(
            host='192.168.1.21',
            user='root',
            passwd='tongmingao',
            db='sgy',
            charset='utf8mb4',
            connect_timeout=Config.DB_TIMEOUT,
            cursorclass=SSCursor,  # 使用服务器端游标
            init_command="SET SESSION wait_timeout=28800"  # 修改为可以设置的变量
        )
        # 移除无法在SESSION设置的变量
        cursor = conn.cursor()
        cursor.execute("SET SESSION sql_mode='STRICT_TRANS_TABLES'")  # 示例可设置变量
        cursor.close()

        logger.info("数据库连接成功")
        return conn
    except MySQLdb.Error as e:
        logger.error(f"数据库连接失败: {e}")
        sys.exit(1)


def get_existing_ids(conn):
    """分批获取已存在的idcard集合（内存优化版）"""
    existing_ids = set()
    try:
        cursor = conn.cursor()

        # 使用UNIX_TIMESTAMP减少数据传输量
        query = "SELECT DISTINCT idcard FROM get_getpersonaldoc"
        cursor.execute(query)

        batch_count = 0
        while True:
            batch = cursor.fetchmany(100000)  # 每次获取10万条
            if not batch:
                break

            existing_ids.update(row[0] for row in batch)
            batch_count += len(batch)

            # 每处理一批释放内存
            del batch
            logger.info(f"已加载 {batch_count} 个idcard到内存")

        logger.info(f"共获取 {len(existing_ids)} 个唯一idcard")
        return existing_ids

    finally:
        cursor.close()


def process_file(filepath, existing_ids, conn):
    """处理单个文件（带重试机制）"""
    idcard = os.path.splitext(os.path.basename(filepath))[0]

    for attempt in range(Config.MAX_RETRIES):
        try:
            # 读取文件内容
            with open(filepath, 'r', encoding='utf-8') as f:
                data_content = f.read()

            # 获取文件修改时间
            file_mtime = datetime.fromtimestamp(os.path.getmtime(filepath))

            cursor = conn.cursor()

            # 情况1: idcard不存在 - 直接导入
            if idcard not in existing_ids:
                try:
                    cursor.execute(
                        """INSERT INTO get_getpersonaldoc 
                        (idcard, data, create_time, update_time, is_delete)
                        VALUES (%s, %s, %s, %s, 0)""",
                        (
                            idcard,
                            data_content,
                            file_mtime,
                            datetime.now()
                        )
                    )
                    existing_ids.add(idcard)
                    return True, "new_idcard"

                except MySQLdb.IntegrityError:
                    # 可能其他进程已插入相同idcard
                    conn.rollback()
                    logger.warning(f"并发冲突，重新检查 {filepath}")
                    existing_ids.add(idcard)
                    continue

            # 情况2: idcard存在 - 精确检查
            cursor.execute(
                """SELECT 1 FROM get_getpersonaldoc 
                WHERE idcard = %s AND data = %s 
                LIMIT 1""",
                (idcard, data_content)
            )
            if cursor.fetchone():
                return False, "duplicate"

            # 插入新记录
            cursor.execute(
                """INSERT INTO get_getpersonaldoc 
                (idcard, data, create_time, update_time, is_delete)
                VALUES (%s, %s, %s, %s, 0)""",
                (
                    idcard,
                    data_content,
                    file_mtime,
                    datetime.now()
                )
            )
            return True, "existing_idcard"

        except MySQLdb.OperationalError as e:
            logger.error(f"数据库操作失败(尝试 {attempt + 1}): {e}")
            if attempt < Config.MAX_RETRIES - 1:
                time.sleep(Config.RETRY_DELAY)
                conn.ping(True)  # 重连
                continue
            raise
        except Exception as e:
            logger.error(f"处理文件 {filepath} 失败: {e}")
            return False, "error"
        finally:
            if 'cursor' in locals():
                cursor.close()


def import_data_safely(directory):
    """安全导入数据主函数"""
    conn = None
    try:
        conn = create_db_connection()
        existing_ids = get_existing_ids(conn)

        # 获取文件列表
        txt_files = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.endswith('.txt')
        ]
        total_files = len(txt_files)

        # 分批处理
        stats = {
            'total': total_files,
            'imported': 0,
            'new_idcard': 0,
            'existing_idcard': 0,
            'duplicate': 0,
            'error': 0
        }

        for i in range(0, total_files, Config.BATCH_SIZE):
            batch = txt_files[i:i + Config.BATCH_SIZE]
            logger.info(f"处理批次 {i // Config.BATCH_SIZE + 1}: {len(batch)} 个文件")

            for j, filepath in enumerate(batch, 1):
                try:
                    imported, reason = process_file(filepath, existing_ids, conn)

                    stats[reason] += 1
                    if imported:
                        stats['imported'] += 1

                    # 定期提交
                    if j % Config.COMMIT_INTERVAL == 0:
                        conn.commit()
                        _log_stats(stats)

                except Exception as e:
                    logger.error(f"处理失败 {filepath}: {e}")
                    stats['error'] += 1
                    conn.rollback()

            # 批次结束提交
            conn.commit()
            _log_stats(stats)

            # 批次间暂停，释放内存
            time.sleep(1)

        return stats

    finally:
        if conn:
            conn.close()


def _log_stats(stats):
    """记录统计信息"""
    logger.info(
        f"进度: {stats['imported'] + stats['duplicate'] + stats['error']}/{stats['total']} | "
        f"新增: {stats['imported']} (新idcard: {stats['new_idcard']}, 已有idcard: {stats['existing_idcard']}) | "
        f"重复: {stats['duplicate']} | 错误: {stats['error']}"
    )


def import_txt_2_sql(directory):
    """
    仅判断idcard
    使用文件创建时间的高性能SQL导入"""

    cursor = conn.cursor()

    # 先查询已存在的idcard
    cursor.execute("SELECT idcard FROM get_getpersonaldoc")
    existing_ids = {row[0] for row in cursor.fetchall()}

    sql = """
    INSERT INTO get_getpersonaldoc 
    (idcard, data, create_time, update_time, is_delete)
    VALUES (%s, %s, %s, %s, 0)
    """

    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    total = len(txt_files)
    imported = 0
    skipped = 0

    for i, filename in enumerate(txt_files, 1):
        idcard = os.path.splitext(filename)[0]

        if idcard in existing_ids:
            skipped += 1
            continue

        filepath = os.path.join(directory, filename)

        # 获取文件创建时间
        file_ctime = datetime.fromtimestamp(os.path.getctime(filepath))

        with open(filepath, 'r', encoding='utf-8') as f:
            data_content = f.read()

        cursor.execute(sql, (
            idcard,
            data_content,
            file_ctime.strftime('%Y-%m-%d %H:%M:%S'),  # 文件创建时间
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ))
        imported += 1

        if i % 1000 == 0:
            conn.commit()
            print(f"进度: {i}/{total}, 已导入: {imported}, 跳过: {skipped}")

    conn.commit()
    print(f"完成: 共处理 {total} 文件, 新增 {imported} 条, 跳过 {skipped} 条")
    cursor.close()
    conn.close()


def import_with_filetime_sql(directory):
    """
    使用文件创建时间的高性能SQL导入
        基于idcard和data双重判断
    """

    cursor = conn.cursor()

    # 先查询已存在的idcard和data组合
    cursor.execute("SELECT idcard, data FROM get_getpersonaldoc")
    existing_records = {(row[0], row[1]) for row in cursor.fetchall()}

    sql = """
    INSERT INTO get_getpersonaldoc 
    (idcard, data, create_time, update_time, is_delete)
    VALUES (%s, %s, %s, %s, 0)
    """

    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    total = len(txt_files)
    imported = 0
    skipped_duplicate = 0
    skipped_other = 0

    for filename in txt_files:
        idcard = os.path.splitext(filename)[0]
        filepath = os.path.join(directory, filename)
        # 读取文件内容
        with open(filepath, 'r', encoding='utf-8') as f:
            data_content = f.read()
        # 检查是否已存在完全相同的记录
        if (idcard, data_content) in existing_records:
            skipped_duplicate += 1
            continue
        # 获取文件修改时间(Modify time)
        file_mtime = datetime.fromtimestamp(os.path.getmtime(filepath))

        # 执行插入
        try:
            cursor.execute(sql, (
                idcard,
                data_content,
                file_mtime.strftime('%Y-%m-%d %H:%M:%S'),
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ))
            imported += 1
            # 添加到已存在集合，避免同批次重复
            existing_records.add((idcard, data_content))

            # 每1000条提交一次
            if imported % 1000 == 0:
                conn.commit()
                print(f"已处理 {imported} 条，跳过 {skipped_duplicate} 条重复")

        except MySQLdb.IntegrityError:
            # 处理可能的并发冲突
            skipped_other += 1
            conn.rollback()

    conn.commit()
    print(f"""导入完成:
        新增记录: {imported}
        跳过完全相同的记录: {skipped_duplicate}
        其他跳过记录: {skipped_other}""")
    cursor.close()
    conn.close()


def import_txt_with_two_stage_check(directory):
    """
    两阶段检查数据导入方案：
    1. 先加载所有已存在的idcard（内存占用小）
    2. 对于idcard已存在的记录，执行精确查询检查data是否重复
    """

    cursor = conn.cursor()
    insert_sql = ''
    # 阶段1：使用迭代器方式获取idcard，避免一次性加载
    logger.info("阶段1: 加载已存在的idcard...")
    start_time = time.time()
    # 使用服务器端游标，避免客户端缓存所有结果
    cursor.execute("SELECT DISTINCT idcard FROM get_getpersonaldoc")
    existing_ids = set()
    batch_size = 100000
    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        existing_ids.update(row[0] for row in rows)
        logger.info(f"已加载 {len(existing_ids)} 个idcard")

    logger.info(f"加载完成! 共 {len(existing_ids)} 个唯一idcard, 耗时: {time.time() - start_time:.2f}秒")

    # 阶段2：优化数据处理
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    total_files = len(txt_files)

    # 使用更高效的数据检查方式
    check_sql = """
           SELECT COUNT(1) FROM get_getpersonaldoc 
           WHERE idcard = %s AND data = %s 
           LIMIT 1
           """

    imported = 0
    skipped_new = 0  # 因idcard不存在而导入的记录
    skipped_duplicate = 0  # 因重复而跳过的记录
    skipped_existing = 0  # 因idcard存在但data不同而导入的记录

    print(f"\n阶段2: 开始处理 {total_files} 个文件...")

    for i, filename in enumerate(txt_files, 1):
        idcard = os.path.splitext(filename)[0]
        filepath = os.path.join(directory, filename)

        # 读取文件内容
        with open(filepath, 'r', encoding='utf-8') as f:
            data_content = f.read()

        # 获取文件修改时间
        file_mtime = datetime.fromtimestamp(os.path.getmtime(filepath))

        # 情况1: idcard不存在 - 直接导入
        if idcard not in existing_ids:
            cursor.execute(insert_sql, (
                idcard,
                data_content,
                file_mtime.strftime('%Y-%m-%d %H:%M:%S'),
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ))
            imported += 1
            skipped_new += 1
            existing_ids.add(idcard)  # 添加到已存在集合

        # 情况2: idcard存在 - 检查具体data是否重复
        else:
            cursor.execute(check_sql, (idcard, data_content))
            exists = cursor.fetchone() is not None

            if exists:
                skipped_duplicate += 1
            else:
                cursor.execute(insert_sql, (
                    idcard,
                    data_content,
                    file_mtime.strftime('%Y-%m-%d %H:%M:%S'),
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ))
                imported += 1
                skipped_existing += 1

        # 进度显示和分批提交
        if i % 1000 == 0:
            conn.commit()
            print(f"已处理: {i}/{total_files} ({i / total_files:.1%}), "
                  f"导入: {imported}, 跳过重复: {skipped_duplicate}")

    # 最终提交
    conn.commit()

    # 打印统计信息
    print(f"\n导入完成!")
    print(f"总文件数: {total_files}")
    print(f"新增记录: {imported} (其中: 全新idcard: {skipped_new}, 已有idcard新data: {skipped_existing})")
    print(f"跳过重复: {skipped_duplicate}")

    cursor.close()
    conn.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python import_script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"错误: 目录不存在 - {directory}")
        sys.exit(1)

    try:
        start_time = time.time()
        stats = import_data_safely(directory)

        logger.info("\n导入完成!")
        logger.info(f"总耗时: {time.time() - start_time:.2f}秒")
        logger.info(f"总文件数: {stats['total']}")
        logger.info(
            f"成功导入: {stats['imported']} (新idcard: {stats['new_idcard']}, 已有idcard新数据: {stats['existing_idcard']})")
        logger.info(f"跳过重复: {stats['duplicate']}")
        logger.info(f"失败文件: {stats['error']}")

    except Exception as e:
        logger.error(f"导入过程发生严重错误: {e}")
        sys.exit(1)
