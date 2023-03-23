# *_* coding : UTF-8 *_*
# 开发团队   ：明日科技
# 开发人员   ：Administrator
# 开发时间   ：2019/7/1  11:29
# 文件名称   ：demo01.py
# 开发工具   ：PyCharm
import math
time=['星期一',  '星期二', '星期三', '星期四','星期五', '星期六', '星期日 ']    # 周日期列表
person=['1821', '752', '951', '1521', '2562', '3522', '4317']        # 周客流列表
print('   电信业务一周高峰客流提示牌                      电信工作人员安排   '.center(30))
for i in  range(len(time)):                         # 按周遍历时间段
    print(time[i],end='')
    quant=math.ceil(int(person[i]) / 200)             # 以200为基数量化客流对比数据
    worker=math.ceil(int(person[i]) / 800)            # 以800为基数量化工作人员数据
    print(('\033[1;35;0m '+chr(0xf0E9)* quant).rjust(40)+'\033[0m',end='')
    print(('\033[1;31;0m '+chr(0xf0E9)* worker).center(80-quant*2)+'\033[0m')
