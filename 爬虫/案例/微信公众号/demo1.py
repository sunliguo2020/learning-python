# -*- coding: utf-8 -*-
"""
 @Time : 2025/2/2 10:31
 @Author : sunliguo
 @Email : sunliguo2006@qq.com
"""
import requests

def download_wechat_video(video_url, output_path):
    # 设置请求头，模拟从微信公众号页面访问
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://mp.weixin.qq.com/",  # 必须添加Referer，否则可能被拒绝访问
    }

    try:
        # 发送GET请求下载视频
        response = requests.get(video_url, headers=headers, stream=True)
        response.raise_for_status()  # 检查请求是否成功

        # 将视频内容写入文件
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"视频已成功下载到：{output_path}")

    except requests.exceptions.RequestException as e:
        print(f"下载失败：{e}")

# 示例使用
if __name__ == "__main__":
    # 替换为实际的微信公众号视频链接
    video_url = "https://mpvideo.qpic.cn/0b786aaaeaaam4ad3235prpfb4gdalyaaaqa.f10002.mp4?dis_k=ab6692e4d80c32f61cb69fb25d6b9904&dis_t=1738473254&play_scene=10120&auth_info=GrTzw/YjT2oG6JfWtAgpPz9uZU45ME9pSVs9a0hWUnwiLQYmcG0wEHdiNk0EMCUc&auth_key=6ec1b665875ee2c9848da44aafd53886&vid=wxv_1269604293192105984&format_id=10002&support_redirect=0&mmversion=false"
    # 替换为保存视频的路径
    output_path = "wechat_video.mp4"

    download_wechat_video(video_url, output_path)