# *_* coding : UTF-8 *_*

# 文件名称   ：demo01.py
# 开发工具   ：PyCharm

import sys
import time
def print_act(word):
    sys.stdout.write("\r")        # 让光标回到行首
    sys.stdout.flush()            # 缓冲区d数据全部输出
    for item in word:             # 遍历整个单词
        sys.stdout.write(item)    # 写到缓冲区
        sys.stdout.flush()        # 输出
        time.sleep(0.3)           # 暂停0.3毫秒
print('访澳旅客   ' + chr(0xf090) +' '+ chr(0xf091)+'  访澳旅客 ')

while True:
    print_act('VISITANTES     VISITANTES')   # 调用print_act()动态输出文字
