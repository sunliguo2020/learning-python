from flask import Flask,render_template,request,url_for,current_app,make_response
import os
from datetime import datetime
import uuid

def gen_rnd_filename():
    '''生成一个随机字符串'''
    return datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex)

app = Flask(__name__)
@app.route('/')
def index():
    '''首页'''
    return render_template('index.html') # 渲染模板

@app.route('/ckupload/', methods=['POST', 'OPTIONS'])
def ckupload():
    """CKEditor 文件上传"""
    error = '' # 初始化变量
    url = ''   # 初始化变量
    callback = request.args.get("CKEditorFuncNum") # 接收回调函数名称
    if request.method == 'POST' and 'upload' in request.files:  # 判断是否上传图片
        fileobj = request.files['upload']  # 接收文件信息
        fname, fext = os.path.splitext(fileobj.filename) # 拆分文件对象信息
        rnd_name = '%s%s' % (gen_rnd_filename(), fext) # 调用函数生成随机文件名
        filepath = os.path.join(current_app.static_folder, 'uploads', rnd_name) # 拼接文件路径
        # 检查路径是否存在，不存在则创建
        dirname = os.path.dirname(filepath)
        if not os.path.exists(dirname):
            try:
                os.makedirs(dirname)      # 如果文件路径不存在，创建路径
            except:
                error = 'ERROR_CREATE_DIR'
        elif not os.access(dirname, os.W_OK): # 如果没有写入权限，提出错误信息
            error = 'ERROR_DIR_NOT_WRITEABLE'
        if not error:
            fileobj.save(filepath)     # 保存文件
            url = url_for('static', filename='%s/%s' % ('uploads', rnd_name)) # 将图片内容显示在CKEditor中
    else:
        error = 'post error'
    # 设置返回文本格式
    res = """<script type="text/javascript">
  window.parent.CKEDITOR.tools.callFunction(%s, '%s', '%s');
</script>""" % (callback, url, error)

    response = make_response(res) # 生成相应
    response.headers["Content-Type"] = "text/html"  # 设置网页内容类型
    return response # 返回相应

if __name__ == "__main__":
    app.run(debug=True) # 运行程序