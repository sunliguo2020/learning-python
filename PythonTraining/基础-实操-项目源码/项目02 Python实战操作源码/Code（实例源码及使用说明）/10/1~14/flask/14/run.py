from flask import Flask, g
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature

app = Flask(__name__) # 实例化Flask类
app.config['SECRET_KEY'] = 'mrsoft' # 设置秘钥
token_serializer = Serializer(app.config['SECRET_KEY'], expires_in=1800) # 实例化Serializer，设置过期时间
auth = HTTPTokenAuth('Bearer') # 基于Token的Bearer方式认证

@auth.verify_token
def verify_token(token):
    '''验证Token'''
    g.username = None
    try:
        data = token_serializer.loads(token) # 将Token反序列化为字典对象
    except SignatureExpired:  # Token 过期失效
        msg = 'token expired'
        app.logger.warning(msg)
        return False
    except BadSignature: # Token 错误
        msg = 'badSignature of token'
        app.logger.warning(msg)
        return False
    except:  # 其他错误
        msg = 'wrong token with unknown reason'
        app.logger.warning(msg)
        return False
    if 'username' in data: # 判断字典对象中是否包含username
        g.username = data['username']
        return True
    return False

@app.route('/login')
def login():
    '''用户登录'''
    username = 'mr'
    password = 'mrsoft'
    token = token_serializer.dumps({'username': username}).decode('utf-8') # 序列化字符串生成Token
    return token

@app.route('/')
@auth.login_required
def index():
    '''首页'''
    return "Hello, %s!" % g.username

if __name__ == '__main__':
    app.run(debug=True)
