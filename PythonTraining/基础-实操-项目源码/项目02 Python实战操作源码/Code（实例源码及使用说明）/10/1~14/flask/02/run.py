from flask import Flask , render_template , session,make_response,flash,request,redirect
import random
import string
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

app = Flask(__name__)     # 实例化Flask类
app.secret_key = "mrsoft" # 设置secret_key

def get_verify_code():
    '''生成验证码图形'''
    code = gene_text() # 调用生成4位验证码的函数
    # 设置图片大小120×50
    width, height = 120, 50
    # 新图片对象
    im = Image.new('RGB',(width, height),'white')
    # 设置字体
    font = ImageFont.truetype('app/static/fonts/arial.ttf', 40)
    # 创建draw对象
    draw = ImageDraw.Draw(im)
    # 绘制字符串
    for item in range(4):
        draw.text((5+random.randint(-3,3)+23*item, 5+random.randint(-3,3)),
                  text=code[item], fill=rndColor(),font=font )
    return im, code

def gene_text():
    '''生成4位验证码'''
    return ''.join(random.sample(string.ascii_letters+string.digits, 4))

def rndColor():
    '''随机颜色'''
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

@app.route('/')
def index():
    return render_template("index.html")  # 渲染页面

@app.route('/login',methods=("GET","POST"))
def login():
    '''登录'''
    if request.method == 'POST':
        code = request.form.get('code','',type=str)
        if code == '':
            flash('验证码不能为空','err')
            return render_template("register.html") # 渲染页面
        if session.get('image').lower() != code:
            flash('验证码错误','err')   
            return render_template("login.html") # 渲染页面
        # 验证码正确
        return redirect("/")  # 渲染页面
    return render_template("login.html") # 渲染页面

@app.route('/code')
def get_code():
    '''获取验证'''
    image, code = get_verify_code() # 调用函数生成验证码图形
    # 图片以二进制形式写入
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把buf_str作为response返回前端，并设置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 将验证码字符串储存在session中
    session['image'] = code
    return response # 返回响应


app.run(debug=True) # 开启调试模式
