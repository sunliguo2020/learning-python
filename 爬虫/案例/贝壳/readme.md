### 密码登录时候post 
到https://clogin.ke.com/authentication/authenticate
```javascript
{
    "username": "15689266711",
    "password": "WQzA8+PRPPq9M+Z0hJPxomrkf0oCUgk0cA+cF8qDt8M8miwbnCsD/8L9WBHhYq/J2cm+8MtAVN2tCOaWC6Qvz5D4zI8SnvtccA/DMB9sVPOvydSAgu7XHa1SNnV3QEuKXyzmy0iVNOn5xlxPKV9KPClVXyh7EKleEZq9sxbHQmo=",
    "encodeVersion": "1"
}
```
主要逆向 password是如何加密的?
### 1、找到加密的地方