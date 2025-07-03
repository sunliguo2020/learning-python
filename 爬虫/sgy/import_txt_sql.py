# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2025/7/3 14:08
"""
import os
import MySQLdb
from datetime import datetime


def import_with_filetime_sql(directory):
    """使用文件创建时间的高性能SQL导入
        基于idcard和data双重判断
    """
    conn = MySQLdb.connect(
        host='192.168.1.21',
        user='root',
        passwd='tongmingao',
        db='sgy',
        charset='utf8mb4'
    )
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


if __name__ == '__main__':
    import_with_filetime_sql('./jiankang/PersonalDoc/2020-06-28')