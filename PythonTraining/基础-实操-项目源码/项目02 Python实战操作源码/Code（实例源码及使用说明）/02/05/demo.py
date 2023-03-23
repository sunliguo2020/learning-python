# *_* coding : UTF-8 *_*
# 文件名称   ：demo.py
# 开发工具   ：PyCharm

import random  # 导入随机模块
surname='赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许'        # 姓氏字库
second='中万斯近元伟丽利国士文连百宏可立成海友南广云基'   # 第二位名字库
# 第三位名字库
third='隆智渝顺乐天杰夫煜兵思霆炜祺亮剀炫翔维瑞韬嘉林庆玮勤栋源路焕霖彩明邦闻朵皓瀚荣奕涓艺'
# 将字库转为列表并去除列表中逗号，例如['赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许']
surname_new=surname.split(',')
second_new=second.split(',')
third_new=third.split(',')
namelist=[]                                 # 保存名字的列表
many = input('请输入需要生成姓名的数量:\n') # 获取输入的数量字符
for i in range(int(many)):                  # 根据数量循环生成指定数量的名字
     data=[2,3]
     namelen=random.choice(data)            # 随机产生2或3
     if namelen==2:                         # 如果是2生成2个字的名字
          newname=random.choice(surname)+random.choice(second)
     else:                                  # 否则生成3个字的名字
          newname =random.choice(surname)+random.choice(second)+ random.choice(third)
     namelist.append(newname)               # 将生成的名字添加至列表中
print('生成的虚拟姓名列表为：\n' + '\n'.join(namelist))
