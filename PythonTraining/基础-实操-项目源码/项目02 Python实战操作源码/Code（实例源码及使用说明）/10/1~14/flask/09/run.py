from flask import Flask,render_template,request,session,redirect,url_for

app = Flask(__name__)
app.secret_key = "mrsoft"

@app.route('/add',methods=['GET','POST'])
def add():
    '''添加酒店信息'''
    if request.method == "POST":
        # 接收数据，使用Session简化数据库操作
        session['hotel_name'] = request.form.get('hotel_name')
        session['hotel_level'] = request.form.get('hotel_level', type=int)
        facilities = request.form.get('hotel_facilities')
        session['hotel_facilities'] = facilities.replace('，', ',')  # 如果用户使用的中文逗号"，",将其转化为英文逗号","
        return redirect(url_for('show')) # 跳转到内容展示页面
    return render_template('add.html')

@app.route('/show')
def show():
    '''展示酒店信息'''
    # 这里使用Session简化从数据库中获取酒店信息
    hotel_name = session['hotel_name']
    hotel_level = session['hotel_level']
    hotel_facilities = session['hotel_facilities']
    return render_template('show.html',hotel_name=hotel_name,hotel_level=hotel_level,hotel_facilities=hotel_facilities)

if __name__ == '__main__':
    app.run(debug=True)