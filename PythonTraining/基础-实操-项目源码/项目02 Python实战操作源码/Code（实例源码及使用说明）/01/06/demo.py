# *_* coding : UTF-8 *_*

# 文件名称   ：demo.py
# 开发工具   ：PyCharm
import  sys
langz=[]
def langline(str):                        # 自定义函数，实现转换英语字符为对应语言文字字符
    langz.clear()                         # 清空临时语言库
    mystr=str.split(';')                  # 分解输入信息
    for item in mystr:
        if item.count(',')>0:
            strii=item.split(',')
            for it in range(int(strii[0],16),int((strii[1]),16)+1):
                langz.append(it)
        else:
            langz.append(item)
def outword(str):                        # 自定义函数，实现语言转换输出
    for item in str:                     # 遍历整个单词
        if ord(item) in mystri:
            start = mystri.index(ord(item))
            outstr=mystrj[start]
            sys.stdout.write(chr(outstr))
            sys.stdout.flush()
        else:
            if ord(item)=='':
                sys.stdout.write(item)
                sys.stdout.flush()
    print('\n')

lange={'01':'希腊文输入','02':'俄文输入','03':'德文输入','04':'丹麦文输入','05':'西班牙文输入','06':'法文输入','07': '荷兰文输入','08':'葡萄牙文输入','09': '意大利文输入','00':'退出输入'}
uni={'01':'0391,03A1;03A3,03A9;0001,0003','02':'0400,042f','03':'0041,005A;0xc4;0xd6;0xdc;0x1e9e','04':'0041,005A;00c6;00d8;00c5','05':'0041,005A;00d1','06':'0041,005A','07': '0041,005A','08':'0041,005A','09': '0041,005A'}
eng=['0041,005A;003A,0040']
# 显示多国语言菜单
print('多国语言文字输出系统')
for key,value in lange.items():     #  遍历字典
    print(key ,value)                #  输出语言菜单
word='1'
langline(''.join(eng))               #  转换英语字符为对应语言文字字符

mystri =[i for i  in langz]
mystrj=[]
while word!='0':
    word= input('请选择需要的国家文字（输入数字即可）：\n')
    word=int(word)
    if word in range(0,10):
        wordid=str(word).zfill(2)
        print('您正在使用',lange.get(wordid),'输入(回车转换大写)：')
        langline(''.join(uni.get(wordid)))
        mystrj = langz
        inword =input().upper()
        outword(inword)
