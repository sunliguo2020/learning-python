# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2025/7/3 14:08
"""
import logging
import sys
import os
from datetime import datetime
import time
import MySQLdb

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)


# 创建数据库连接
def create_db_connection():
    """创建数据库连接"""
    try:
        conn = MySQLdb.connect(
            host='192.168.1.21',
            user='root',
            passwd='tongmingao',
            db='sgy',
            charset='utf8mb4'
        )
        logger.info("数据库连接成功")
        return conn
    except MySQLdb.Error as e:
        logger.error(f"数据库连接失败: {e}")
        sys.exit(1)


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

    # 阶段1：获取所有已存在的idcard（去重后）
    print("阶段1: 加载已存在的idcard...")
    start_time = time.time()
    cursor.execute("SELECT DISTINCT idcard FROM get_getpersonaldoc")
    existing_ids = {row[0] for row in cursor.fetchall()}
    print(f"加载完成! 共 {len(existing_ids)} 个唯一idcard, 耗时: {time.time() - start_time:.2f}秒")

    # 准备SQL语句
    insert_sql = """
    INSERT INTO get_getpersonaldoc 
    (idcard, data, create_time, update_time, is_delete)
    VALUES (%s, %s, %s, %s, 0)
    """

    check_sql = """
    SELECT 1 FROM get_getpersonaldoc 
    WHERE idcard = %s AND data = %s 
    LIMIT 1
    """

    # 遍历文件
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    total_files = len(txt_files)
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
    # 连接数据库
    conn = MySQLdb.connect(
        host='192.168.1.21',
        user='root',
        passwd='tongmingao',
        db='sgy',
        charset='utf8mb4'
    )

    import sys

    if len(sys.argv) < 2:
        print("Usage: python import_script.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"错误: 目录不存在 - {directory}")
        sys.exit(1)

    import_txt_with_two_stage_check(directory)
