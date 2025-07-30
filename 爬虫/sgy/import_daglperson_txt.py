# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2025/7/30 8:28
优化版数据导入脚本 - 线程安全版本
特点：
1. 目录和表名均为必填项
2. 每个线程独立数据库连接
3. 内存友好的批处理
4. 完善的错误处理
"""

import logging
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import MySQLdb
from MySQLdb import Error as MySQLdbError
import psutil

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
    # 运行参数
    BATCH_SIZE = 100  # 每批处理文件数
    COMMIT_INTERVAL = 1000  # 每多少条提交一次
    MAX_RETRIES = 3  # 最大重试次数
    RETRY_DELAY = 10  # 重试延迟(秒)
    DB_TIMEOUT = 30  # 数据库操作超时(秒)
    MAX_WORKERS = 4  # 最大线程数（根据服务器配置调整）
    DELETE_PROCESSED_FILES = True  # 是否删除已处理的文件
    DB_CONFIG = {
        'host': '192.168.1.21',
        'user': 'root',
        'passwd': 'tongmingao',
        'db': 'sgy',
        'charset': 'utf8mb4',
        'connect_timeout': 30
    }


class DatabaseManager:
    """数据库连接管理"""

    @staticmethod
    def create_connection():
        """创建新的数据库连接"""
        try:
            conn = MySQLdb.connect(**Config.DB_CONFIG)
            conn.autocommit(False)
            return conn
        except MySQLdbError as e:
            logger.error(f"数据库连接失败: {e}")
            raise

    @staticmethod
    def get_existing_ids(conn, table_name):
        """获取已存在的personid集合（分批处理）"""
        existing_ids = set()
        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT DISTINCT personid FROM {table_name}")

            while True:
                batch = cursor.fetchmany(10000)
                if not batch:
                    break
                existing_ids.update(row[0] for row in batch)
                logger.info(f"已加载 {len(existing_ids)} 个personid")
                # 定期释放内存
                if len(existing_ids) % 100000 == 0:
                    time.sleep(0.1)

            logger.info(f"共获取 {len(existing_ids)} 个唯一personid")
            return existing_ids
        finally:
            if cursor:
                cursor.close()


class DataImporter:
    """数据导入处理器"""

    def __init__(self, table_name):
        self.table_name = table_name
        self.stats = {
            'total': 0,
            'imported': 0,
            'new_personid': 0,
            'existing_personid': 0,
            'duplicate': 0,
            'error': 0,
            'deleted': 0,
            'duplicate_deleted': 0,
            'start_time': time.time()
        }

    def process_batch(self, batch_files, existing_ids):
        """处理文件批次（线程安全版本）"""
        batch_stats = {
            'imported': 0,
            'new_personid': 0,
            'existing_personid': 0,
            'duplicate': 0,
            'error': 0,
            'deleted': 0,
            'duplicate_deleted': 0
        }

        # 每个线程使用独立连接
        conn = None
        try:
            conn = DatabaseManager.create_connection()
            insert_data = []
            delete_files = []

            for filepath in batch_files:
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data_content = f.read()

                    # 从文件名中提取personid（去掉.txt扩展名）
                    personid = int(os.path.splitext(os.path.basename(filepath))[0])
                    file_mtime = datetime.fromtimestamp(os.path.getmtime(filepath))

                    # 检查是否已存在（使用当前连接）
                    with conn.cursor() as cursor:
                        cursor.execute(
                            f"""SELECT 1 FROM {self.table_name} 
                            WHERE personid=%s AND data=%s LIMIT 1""",
                            (personid, data_content)
                        )
                        exists = cursor.fetchone()

                    if exists:
                        batch_stats['duplicate'] += 1
                        if Config.DELETE_PROCESSED_FILES:
                            delete_files.append(filepath)
                            batch_stats['duplicate_deleted'] += 1
                        continue

                    # 准备插入数据
                    insert_data.append((
                        personid, data_content, file_mtime, datetime.now()
                    ))

                    # 更新统计
                    if personid in existing_ids:
                        batch_stats['existing_personid'] += 1
                    else:
                        batch_stats['new_personid'] += 1
                        existing_ids.add(personid)

                    if Config.DELETE_PROCESSED_FILES:
                        delete_files.append(filepath)
                        batch_stats['deleted'] += 1

                except Exception as e:
                    logger.error(f"处理文件 {filepath} 失败: {e}")
                    batch_stats['error'] += 1

            # 批量插入
            if insert_data:
                with conn.cursor() as cursor:
                    cursor.executemany(
                        f"""INSERT INTO {self.table_name} 
                        (personid, data, create_time, update_time, is_delete)
                        VALUES (%s, %s, %s, %s, 0)""",
                        insert_data
                    )
                    batch_stats['imported'] = len(insert_data)
                conn.commit()

            # 批量删除文件
            if delete_files:
                actual_deleted = self._batch_delete_files(delete_files)
                if actual_deleted != len(delete_files):
                    logger.warning(f"预期删除 {len(delete_files)} 文件，实际删除 {actual_deleted}")

        except Exception as e:
            logger.error(f"批次处理失败: {e}")
            if conn:
                conn.rollback()
            batch_stats['error'] += len(batch_files)
        finally:
            if conn:
                conn.close()

        return batch_stats

    def _batch_delete_files(self, filepaths):
        """批量删除文件"""
        deleted_count = 0
        for filepath in filepaths:
            try:
                if os.path.exists(filepath):
                    os.remove(filepath)
                    deleted_count += 1
            except Exception as e:
                logger.error(f"删除文件失败 {filepath}: {e}")
        return deleted_count

    def import_data(self, directory):
        """主导入方法"""
        try:
            # 获取文件列表（使用生成器节省内存）
            txt_files = [
                os.path.join(directory, f)
                for f in os.listdir(directory)
                if f.endswith('.txt') and f[:-4].isdigit()  # 确保文件名是数字.txt格式
            ]
            self.stats['total'] = len(txt_files)

            if not txt_files:
                logger.info("没有找到可处理的.txt文件")
                return self.stats

            logger.info(f"开始处理 {self.stats['total']} 个文件...")
            logger.info(f"目标表：{self.table_name}")
            logger.info(f"当前内存使用: {self._get_memory_usage()}MB")

            # 主数据库连接用于获取existing_ids
            main_conn = DatabaseManager.create_connection()
            existing_ids = DatabaseManager.get_existing_ids(main_conn, self.table_name)
            main_conn.close()

            # 多线程处理
            with ThreadPoolExecutor(max_workers=Config.MAX_WORKERS) as executor:
                futures = []
                for i in range(0, self.stats['total'], Config.BATCH_SIZE):
                    batch = txt_files[i:i + Config.BATCH_SIZE]
                    future = executor.submit(
                        self.process_batch,
                        batch,
                        existing_ids  # 每个线程会创建自己的连接
                    )
                    futures.append(future)
                    # 控制内存使用
                    if len(futures) >= Config.MAX_WORKERS * 2:
                        self._process_futures(futures)

                # 处理剩余任务
                self._process_futures(futures)

            return self.stats

        except Exception as e:
            logger.error(f"导入过程发生严重错误: {e}")
            raise
        finally:
            self._log_final_stats()

    def _process_futures(self, futures):
        """处理已完成的任务"""
        for future in as_completed(futures):
            batch_stats = future.result()
            self._update_stats(batch_stats)
            self._log_progress()
            # 从列表中移除已处理的任务
            futures.remove(future)

    def _update_stats(self, batch_stats):
        """更新统计信息"""
        for k, v in batch_stats.items():
            self.stats[k] += v

    def _log_progress(self):
        """记录进度"""
        elapsed = time.time() - self.stats['start_time']
        files_processed = self.stats['imported'] + self.stats['duplicate'] + self.stats['error']
        progress = files_processed / self.stats['total']

        logger.info(
            f"进度: {files_processed}/{self.stats['total']} ({progress:.1%}) | "
            f"新增: {self.stats['imported']} | "
            f"重复: {self.stats['duplicate']} | "
            f"错误: {self.stats['error']} | "
            f"删除: {self.stats['deleted'] + self.stats['duplicate_deleted']} | "
            f"内存: {self._get_memory_usage()}MB | "
            f"耗时: {elapsed:.1f}s"
        )

    def _log_final_stats(self):
        """记录最终统计"""
        elapsed = time.time() - self.stats['start_time']
        logger.info("\n导入完成!")
        logger.info(f"目标表: {self.table_name}")
        logger.info(f"总耗时: {elapsed:.2f}秒")
        logger.info(f"总文件数: {self.stats['total']}")
        logger.info(
            f"成功导入: {self.stats['imported']} "
            f"(新personid: {self.stats['new_personid']}, "
            f"已有personid新数据: {self.stats['existing_personid']})"
        )
        logger.info(f"跳过重复记录: {self.stats['duplicate']} (已删除文件: {self.stats['duplicate_deleted']})")
        logger.info(f"失败文件: {self.stats['error']}")
        logger.info(f"总删除文件数: {self.stats['deleted'] + self.stats['duplicate_deleted']}")
        logger.info(f"峰值内存使用: {self._get_memory_usage()}MB")

    @staticmethod
    def _get_memory_usage():
        """获取当前进程内存使用(MB)"""
        return psutil.Process().memory_info().rss / 1024 / 1024


def main():
    if len(sys.argv) < 3:
        print("Usage: python import_script.py <directory> <table_name> [--keep-files]")
        print("Arguments:")
        print("<directoyr> 包含.txt 文件的目录路径（必填）")
        print("<table_name> 目标数据库表名（必填）")
        print("Options:")
        print("  --keep-files  保留所有源文件(不删除)")
        sys.exit(1)

    directory = sys.argv[1]
    table_name = sys.argv[2]
    Config.DELETE_PROCESSED_FILES = "--keep-files" not in sys.argv

    if not os.path.isdir(directory):
        print(f"错误: 目录不存在 - {directory}")
        sys.exit(1)

    if not table_name.strip():
        print("错误: 表名不能为空")
        sys.exit(1)

    try:
        importer = DataImporter(table_name)
        stats = importer.import_data(directory)
        sys.exit(0 if stats['error'] == 0 else 1)
    except Exception as e:
        logger.error(f"导入过程发生严重错误: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()