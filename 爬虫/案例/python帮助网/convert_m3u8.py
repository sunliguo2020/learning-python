# -*- coding: utf-8 -*-
"""
 @Time : 2024/12/10 22:32
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
 1、下载ts文件
 2、转换为mp4
"""
import os
import urllib.parse
import urllib.request
import shutil
import subprocess
import tempfile

import requests


def download_file(url, local_filename):
    """
    下载并保存文件
    @param url:
    @param local_filename:
    @return:
    """
    # with urllib.request.urlopen(url) as response, open(local_filename, 'wb') as out_file:
    with requests.get(url) as response, open(local_filename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)


def process_m3u8(m3u8_path, base_url=None, download_dir=None):
    """
    通过分析m3u8文件中的ts文件url，下载保存
    @param m3u8_path:
    @param base_url:
    @param download_dir:
    @return:
    """
    # 包含ts文件url的列表
    ts_files = []
    with open(m3u8_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith('#EXTINF:'):
                # 下一行或当前行末尾可能包含ts文件的路径
                next_line = file.readline().strip()
                if not next_line.startswith('#'):
                    ts_url = next_line if not next_line.startswith('#') else line.split(',')[-1]
                    if base_url:
                        ts_url = urllib.parse.urljoin(base_url, ts_url)
                    ts_filename = os.path.join(download_dir, os.path.basename(urllib.parse.urlparse(ts_url).path))
                    ts_files.append(ts_filename)
                    if not os.path.exists(ts_filename):
                        download_file(ts_url, ts_filename)

    return ts_files


def merge_ts_to_mp4(ts_files, output_mp4):
    """
    合并ts文件为mp4
    @param ts_files:
    @param output_mp4:
    @return:
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as file_list:
        for ts_file in ts_files:
            file_list.write(f'file \'{ts_file}\'\n')
        file_list_path = file_list.name

    ffmpeg_command = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', file_list_path,
        '-c', 'copy',
        output_mp4
    ]
    # subprocess.run(ffmpeg_command, check=True)

    # os.remove(file_list_path)


def main(root_dir, base_url=None, output_mp4_prefix='output'):
    for subdir, _, _ in os.walk(root_dir):
        for filename in os.listdir(subdir):
            if filename.endswith('.m3u8'):
                m3u8_path = os.path.join(subdir, filename)

                download_dir = subdir
                print(f"准备下载:{m3u8_path}位置：{download_dir}")
                try:
                    ts_files = process_m3u8(m3u8_path, base_url=base_url, download_dir=download_dir)
                    print(ts_files)
                    output_mp4 = os.path.join(subdir,
                                              f'{output_mp4_prefix}_{os.path.basename(filename).rsplit(".", 1)[0]}.mp4')
                    # merge_ts_to_mp4(ts_files, output_mp4)
                finally:
                    # shutil.rmtree(download_dir)
                    pass


if __name__ == '__main__':
    root_directory = './'  # 替换为你的根目录路径
    base_url_for_ts = 'http://49.233.211.165/'  # 如果ts文件是网络URL，提供基URL；否则为None
    main(root_directory, base_url_for_ts)
