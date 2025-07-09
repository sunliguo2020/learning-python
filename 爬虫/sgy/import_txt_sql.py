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
5、只有在成功导入或记录已存在时删除文件
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
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('data_import.log')
    ]
)
logger = logging.getLogger(__name__)


class Config:
    """配置参数类"""
    BATCH_SIZE = 500  # 每批处理文件数
    COMMIT_INTERVAL = 100  # 每多少条提交一次
    MAX_RETRIES = 3  # 最大重试次数
    RETRY_DELAY = 10  # 重试延迟(秒)
    DB_TIMEOUT = 30  # 数据库操作超时(秒)
    IDCARD_BATCH = 100000  # ID查询批次大小
    DELETE_PROCESSED_FILES = True  # 是否删除已处理的文件


class DataImporter:
    """数据导入处理器"""

    def __init__(self):
        self.conn = None
        self.stats = {
            'total': 0,
            'imported': 0,
            'new_idcard': 0,
            'existing_idcard': 0,
            'duplicate': 0,
            'error': 0,
            'deleted': 0, # 记录删除文件数
            'duplicate_deleted': 0 # 记录重复并删除的文件数
        }

    def create_db_connection(self):
        """创建数据库连接"""
        try:
            self.conn = MySQLdb.connect(
                host='192.168.1.21',
                user='root',
                passwd='tongmingao',
                db='sgy',
                charset='utf8mb4',
                connect_timeout=Config.DB_TIMEOUT,
                cursorclass=SSCursor,
                init_command="SET SESSION wait_timeout=28800"
            )
            self.conn.autocommit(False)
            logger.info("数据库连接成功")
        except MySQLdb.Error as e:
            logger.error(f"数据库连接失败: {e}")
            raise

    def get_existing_ids(self):
        """分批获取已存在的idcard集合"""
        existing_ids = set()
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT DISTINCT idcard FROM get_getpersonaldoc")

            while True:
                batch = cursor.fetchmany(Config.IDCARD_BATCH)
                if not batch:
                    break
                existing_ids.update(row[0] for row in batch)
                logger.info(f"已加载 {len(existing_ids)} 个idcard")

            logger.info(f"共获取 {len(existing_ids)} 个唯一idcard")
            return existing_ids
        finally:
            if cursor:
                cursor.close()

    def safe_delete_file(self, filepath):
        """安全删除文件"""
        try:
            logger.debug(f"尝试删除文件: {filepath}")
            logger.debug(f"文件存在: {os.path.exists(filepath)}")
            logger.debug(f"文件权限: {oct(os.stat(filepath).st_mode)[-3:]}")

            if os.path.exists(filepath):
                os.remove(filepath)
                logger.info(f"成功删除文件: {filepath}")
                return True
            logger.warning(f"文件不存在: {filepath}")
            return False
        except Exception as e:
            logger.error(f"删除文件失败 {filepath}: {str(e)}")
            return False

    def process_file(self, filepath, existing_ids):
        """处理单个文件"""
        idcard = os.path.splitext(os.path.basename(filepath))[0]
        should_delete = False  # 标记是否需要删除文件
        result = False
        reason = 'error'
        for attempt in range(Config.MAX_RETRIES):
            cursor = None
            try:
                # 读取文件内容
                with open(filepath, 'r', encoding='utf-8') as f:
                    data_content = f.read()

                file_mtime = datetime.fromtimestamp(os.path.getmtime(filepath))
                cursor = self.conn.cursor()

                # idcard不存在则直接导入
                if idcard not in existing_ids:
                    try:
                        cursor.execute(
                            """INSERT INTO get_getpersonaldoc 
                            (idcard, data, create_time, update_time, is_delete)
                            VALUES (%s, %s, %s, %s, 0)""",
                            (idcard, data_content, file_mtime, datetime.now())
                        )
                        existing_ids.add(idcard)
                        result, reason = True, "new_idcard"
                        should_delete = True  # 导入成功，标记删除
                        break
                    except MySQLdb.IntegrityError:
                        self.conn.rollback()
                        existing_ids.add(idcard)
                        reason = "duplicate"
                        continue

                # 情况2：idcard存在 - 检查是否已存在相同记录
                cursor.execute(
                    """SELECT 1 FROM get_getpersonaldoc 
                    WHERE idcard=%s AND data=%s LIMIT 1""",
                    (idcard, data_content)
                )
                if cursor.fetchone():
                    result, reason = False, "duplicate"
                    should_delete = True  # 重复记录，标记删除
                    break
                else:
                    # 插入新记录
                    cursor.execute(
                        """INSERT INTO get_getpersonaldoc 
                        (idcard, data, create_time, update_time, is_delete)
                        VALUES (%s, %s, %s, %s, 0)""",
                        (idcard, data_content, file_mtime, datetime.now())
                    )
                    result, reason = True, "existing_idcard"
                    should_delete = True
                    break

            except MySQLdb.OperationalError as e:
                logger.error(f"数据库操作失败(尝试 {attempt + 1}): {e}")
                if attempt < Config.MAX_RETRIES - 1:
                    time.sleep(Config.RETRY_DELAY)
                    self.conn.ping(True)
                    continue
                raise
            except Exception as e:
                logger.error(f"处理文件 {filepath} 失败: {e}")
                reason = "error"
                break
            finally:
                if cursor:
                    cursor.close()
        # 根据条件删除文件
        if Config.DELETE_PROCESSED_FILES and should_delete:
            if self.safe_delete_file(filepath):
                if reason == "duplicate":
                    self.stats['duplicate_deleted'] += 1
                else:
                    self.stats['deleted'] +=1
            logger.debug(f"删除文件 {filepath}")

        return result, reason

    def import_data(self, directory):
        """主导入方法"""
        try:
            self.create_db_connection()
            existing_ids = self.get_existing_ids()

            # 获取文件列表
            txt_files = [
                os.path.join(directory, f)
                for f in os.listdir(directory)
                if f.endswith('.txt')
            ]
            self.stats['total'] = len(txt_files)

            # 分批处理
            for i in range(0, self.stats['total'], Config.BATCH_SIZE):
                batch = txt_files[i:i + Config.BATCH_SIZE]
                logger.info(f"处理批次 {i // Config.BATCH_SIZE + 1}: {len(batch)} 个文件")

                for j, filepath in enumerate(batch, 1):
                    try:
                        imported, reason = self.process_file(filepath, existing_ids)
                        self.stats[reason] += 1
                        if imported:
                            self.stats['imported'] += 1

                        # 定期提交
                        if j % Config.COMMIT_INTERVAL == 0:
                            self.conn.commit()
                            self._log_stats()

                    except Exception as e:
                        logger.error(f"处理失败 {filepath}: {e}")
                        self.stats['error'] += 1
                        self.conn.rollback()

                # 批次结束提交
                self.conn.commit()
                self._log_stats()
                time.sleep(1)  # 批次间暂停

            return self.stats

        finally:
            if self.conn:
                self.conn.close()

    def _log_stats(self):
        """记录统计信息"""
        logger.info(
            f"进度: {self.stats['imported'] + self.stats['duplicate'] + self.stats['error']}/{self.stats['total']} | "
            f"新增: {self.stats['imported']} (新idcard: {self.stats['new_idcard']}, 已有idcard: {self.stats['existing_idcard']}) | "
            f"重复记录: {self.stats['duplicate']} (已删除文件: {self.stats['duplicate_deleted']}) | "
            f"错误: {self.stats['error']} | "
            f"总删除文件: {self.stats['deleted'] + self.stats['duplicate_deleted']}"
        )


def main():
    if len(sys.argv) < 2:
        print("Usage: python import_script.py <directory> [--keep-files]")
        print("Options:")
        print("  --keep-files  保留所有源文件(不删除)")
        sys.exit(1)

    # 解析参数
    directory = sys.argv[1]
    Config.DELETE_PROCESSED_FILES = "--keep-files" not in sys.argv

    if not os.path.isdir(directory):
        print(f"错误: 目录不存在 - {directory}")
        sys.exit(1)

    try:
        start_time = time.time()
        importer = DataImporter()
        stats = importer.import_data(directory)

        logger.info("\n导入完成!")
        logger.info(f"总耗时: {time.time() - start_time:.2f}秒")
        logger.info(f"总文件数: {stats['total']}")

        logger.info(
            f"成功导入: {stats['imported']} (新idcard: {stats['new_idcard']}, 已有idcard新数据: {stats['existing_idcard']})")
        logger.info(f"跳过重复记录: {stats['duplicate']} (已删除文件: {stats['duplicate_deleted']})")
        logger.info(f"失败文件: {stats['error']}")
        logger.info(f"总删除文件数: {stats['deleted'] + stats['duplicate_deleted']}")

    except Exception as e:
        logger.error(f"导入过程发生严重错误: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
