from PIL import Image

def get_char(r,g,b,a=256):
    if a == 0:
        return ' '
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
    length = len(ascii_str)
    unit = 256/length
    return ascii_str[int(gray/unit)]


if __name__ == "__main__":
    WIDTH = 80
    HEIGHT = 40
    ascii_str = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    im = Image.open('face.png')
    im = im.resize((WIDTH,HEIGHT))
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i))) # (r,g,b,a)
        txt += '\n'

    print(txt)
    # 字符画输出到文件
    with open("output.txt", 'w') as f:
        f.write(txt)