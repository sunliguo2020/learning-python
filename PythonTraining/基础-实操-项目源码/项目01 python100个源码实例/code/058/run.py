from PIL import Image
import argparse


def get_char(r,g,b,a=256):
    if a == 0:
        return ' '
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
    length = len(ascii_str)
    unit = 256/length
    return ascii_str[int(gray/unit)]


if __name__ == "__main__":
    # 命令行输入参数处理
    parser = argparse.ArgumentParser()
    parser.add_argument('file')  # 输入文件
    parser.add_argument('-o', '--output')  # 输出文件
    parser.add_argument('--width', type=int, default=80)  # 输出字符画宽
    parser.add_argument('--height', type=int, default=80)  # 输出字符画高

    # 获取参数
    args = parser.parse_args()
    IMG = args.file
    WIDTH = args.width
    HEIGHT = args.height
    OUTPUT = args.output

    ascii_str = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT))
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i))) # (r,g,b,a)
        txt += '\n'

    print(txt)
    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
