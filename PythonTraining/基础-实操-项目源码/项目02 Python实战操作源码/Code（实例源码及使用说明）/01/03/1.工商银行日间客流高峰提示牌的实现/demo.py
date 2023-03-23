# *_* coding : UTF-8 *_*
# 文件名称   ：demo01.py
# 开发工具   ：PyCharm
import math
# 银行工作时间
time=['08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00']
person=['572','1236','7634','8799','9876','4562','1038','453']         # 时间段客流人数
print('工商银行日间客流高峰提示牌'.center(30))                             # 输出标题
for i in  range(len(time)-1):                                  # 遍历时间段
    print(time[i],':',time[i+1],end='')                        # 输出时间段
    quant=math.ceil(int(person[i]) / 600 )     # 以600为基数量化客流对比数据
    print(('\033[1;33;0m '+chr(0xf04a)* quant).rjust(30)+'\033[0m')
