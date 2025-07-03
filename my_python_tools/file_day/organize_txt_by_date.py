#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 2020-04-19

@author: sunliguo
功能：将指定目录中的.txt文件按照修改日期自动分类到对应日期文件夹中
"""

import os
import shutil
import time
from typing import List, Tuple


def get_user_confirmation(prompt: str) -> bool:
    """获取用户确认
    参数:
        prompt: 提示信息
    返回:
        bool: 用户确认结果(True/False)
    """
    while True:
        response = input(f"{prompt} (y/n): ").lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        print("请输入 'y' 或 'n'.")


def mymove_file(src: str, dst: str, method: str = 'rename') -> bool:
    """
    移动文件(带错误处理）
    Parameters
    ----------
    src：源文件路径
    dst：目标文件路径
    method:移动方式（‘rename'快速但不跨文件系统 'copy'慢但跨文件系统)

    Returns
        bool:是否成功
    -------

    """
    # 检查源文件是否存在
    if not os.path.isfile(src):
        print('%s not exist!' % src)
        return False
    try:
        # 分离目标路径和文件名
        fpath, fname = os.path.split(dst)
        # 如果目标目录不存在则创建
        if not os.path.exists(fpath):
            os.makedirs(fpath)
            print('create dir {0}'.format(fpath))
        # 根据指定方法移动文件
        if method == 'rename':
            os.rename(src, dst)  # 重命名方式（同文件系统)
        else:
            shutil.move(src, dst)  # 复制+删除方式（跨文件系统）
        print('move {0}->{1}'.format(src, dst))
        return True
    except Exception as e:
        print(f"移动文件{src}:出错{str(e)}")
        return False


def organize_files_by_date(directory: str = '.', dry_run: bool = False) -> Tuple[int, int, List[str]]:
    """
    按修改日期整理文件
    参数:
        directory: 要整理的目录路径
        dry_run: 试运行模式(只显示不实际执行)
    返回:
        (总文件数, 成功移动数, 错误文件列表)
    """
    # 检查目录是否存在
    if not os.path.isdir(directory):
        print(f'错误: 目录 {directory} 不存在!')
        return (0, 0, [])

    # 获取目录中所有.txt文件
    try:
        file_list = [
            f for f in os.listdir(directory)
            if f.endswith('.txt') and os.path.isfile(os.path.join(directory, f))
        ]
    except Exception as e:
        print(f'读取目录出错: {str(e)}')
        return (0, 0, [])

    total_files = len(file_list)
    if total_files == 0:
        print('未找到需要整理的.txt文件。')
        return (0, 0, [])

    print(f'找到 {total_files} 个需要整理的.txt文件。')

    moved_files = 0  # 成功移动计数
    error_files = []  # 错误文件列表

    # 遍历处理每个文件
    for i, filename in enumerate(file_list, 1):
        file_full_path = os.path.join(directory, filename)

        try:
            # 获取文件修改时间
            mtime = os.stat(file_full_path).st_mtime
            # 格式化为YYYY-MM-DD格式
            file_modify_date = time.strftime('%Y-%m-%d', time.localtime(mtime))

            # 构建目标路径(按日期分类)
            dst_dir = os.path.join(directory, file_modify_date)
            dst_path = os.path.join(dst_dir, filename)

            # 打印处理信息
            print(f'\n文件 {i}/{total_files}: {filename}')
            print(f'  最后修改时间: {file_modify_date}')
            print(f'  将移动到: {dst_path}')

            # 如果不是试运行模式则实际执行移动
            if not dry_run:
                if move_file(file_full_path, dst_path):
                    moved_files += 1
                else:
                    error_files.append(filename)

        except Exception as e:
            print(f'处理文件 {filename} 出错: {str(e)}')
            error_files.append(filename)

    return (total_files, moved_files, error_files)


def main():
    """主函数"""
    print("\n=== 文件整理工具 ===")
    print("功能: 将.txt文件按修改日期自动分类到对应日期文件夹\n")

    # 获取要整理的目录路径
    directory = input("输入要整理的目录路径(默认当前目录): ").strip()
    if not directory:
        directory = '.'  # 默认当前目录

    # 确认是否试运行
    dry_run = False
    if get_user_confirmation("是否试运行(只显示不实际移动文件)?"):
        dry_run = True
        print("\n注意: 处于试运行模式,不会实际移动文件!")

    # 执行文件整理
    print("\n开始整理文件...")
    total, moved, errors = organize_files_by_date(directory, dry_run)

    # 输出结果统计
    print("\n=== 整理结果 ===")
    print(f"总文件数: {total}")
    print(f"成功移动: {moved}")
    print(f"失败文件: {len(errors)}")

    if errors:
        print("\n失败文件列表:")
        for f in errors:
            print(f"  - {f}")

    if dry_run:
        print("\n提示: 本次为试运行模式,未实际移动文件")


if __name__ == '__main__':
    main()
