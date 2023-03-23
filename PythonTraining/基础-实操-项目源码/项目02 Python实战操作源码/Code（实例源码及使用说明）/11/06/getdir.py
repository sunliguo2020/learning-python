import os                                                 # 导入系统模块
import sys                                                # 导入操作系统模块
import re                                                 # 导入正则表达式模块
d = os.path.dirname(os.path.realpath(sys.argv[0]))    # 获取当前文件所在路径
d = re.sub(r'\\', '/', d)                                # 将路径中的分隔符\替换为/
print("【修改后】获取的路径：",d)
