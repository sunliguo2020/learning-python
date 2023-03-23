# *_* coding : UTF-8 *_*
# 文件名称   ：demo.py
# 开发工具   ：PyCharm

def inputbox(showstr, showorder, lengh):
    instr = input(showstr)
    if len(instr) != 0:             # 如果输入内容的长度不为0时
        # 模式1检测输入的字符是否为数字并检测是不是0
        if showorder == 1:
            if str.isdigit(instr):  # 检测输入的字符串是否只由数字组成
                if instr == '0':    # 如果输入的字符是0时
                    print("\033[1;31;40m 输入为零，请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")
                return "0"
        # 模式2检测输入的字符是否为字母并检测输入的字母是不是3个
        if showorder == 2:
            if str.isalpha(instr):   # 检测输入的字符串是否只由字母组成
                if len(instr) != 3:  # 如果输入的不是3个字母
                    print("\033[1;31;40m必须输入三个字母，请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")
                return "0"
        # 模式3检测输入的字符是否为数字并检测输入的字符长度与目标数字是否相同
        if showorder == 3:
            if str.isdigit(instr):        # 检测输入的字符串是否只由数字组成
                if len(instr) != lengh:   # 如果输入的数字字符串长度与目标数字不同时
                    print("\033[1;31;40m必须输入" + str(lengh) + "个数字，请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")
                return "0"
    else:
        print("\033[1;31;40m输入为空，请重新输入！！\033[0m")
        return "0"

a=inputbox('请输入数据为零、数字、字母等:',1,2)      # 选择模式1，此时lengh参数无效
print('返回值为：',a)                                # 打印返回值