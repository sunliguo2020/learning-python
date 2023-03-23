from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    book = "《Python 从入门到项目实践》"
    content = '''
    一书从入门学习者的角度出发，通过简洁有趣的语言、丰富多彩的实例、挑战大脑的任务、贴近开发实战的项目，
    循序渐进地让读者在实践中学习，在实践中提升实际开发能力。全书共分7 篇：基础篇、进阶篇、高级篇、框架篇、游戏开发篇、
    人工智能开发篇和商业项目篇，内容包括：踏上Python 之旅、熟悉PyCharm 开发环境、Python 输入与输出、变量与基本数据类型、
    运算符、列表和元组、字符串与正则表达式、流程控制、循环结构语句、字典与集合、类和对象、模块、文件与IO、
    使用Python 操作数据库、进程和线程、网络编程、异常处理与程序调试、常用的GUI 框架、pygame 游戏框架、网络爬虫框架、
    Flask Web 框架的使用、Django Web 框架的使用、谷歌小恐龙游戏、飞机大战游戏、微信跳一跳辅助工具、汽车之家图片抓取工具、
    AI 图像识别工具、e 起去旅行网站、看店宝（京东版）。
    '''
    return render_template('index.html',book=book,content=content)

@app.route('/comment')
def comment():
    goods_id = request.args.get('goods_id')
    # 省略根据商品ID查询评论表的步骤
    comments = [
        {'id':1,'username':'张三','comment':'通俗易懂，一个小白，学起来豪不费力，期待看完的那一刻'},
        {'id':2,'username':'李四','comment':'非常好的工具书。深入学习。紧追时代潮流'},
        {'id':3,'username':'王五','comment':'彩色印刷，质量很好，赞一个'}
    ]
    return render_template("comment.html", comments=comments)

if __name__ == "__main__":
    app.run(debug=True)  # 开启调试模式
