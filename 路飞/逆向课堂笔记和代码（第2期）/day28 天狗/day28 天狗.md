# day28 xx天狗（最后一发）

目标：逆向app实现大商天狗的 自动注册

版本：v2.6.28



> 提示：最新发送短信的接口已停用，收不到短信，但是可以先来分析他的算法。





## 1.抓包

发送短信：

![image-20220419170513302](assets/image-20220419170513302.png)

![image-20220419170702679](assets/image-20220419170702679.png)



要解决的问题：

- 请求体：sign签名（主）
- 请求头：
  - tgs_uuid
  - key





点击注册：

![image-20220419170143516](assets/image-20220419170143516.png)

![image-20220419170319367](assets/image-20220419170319367.png)



要解决的问题：

- 请求体：密码处理
- 请求头：
  - tgs_uuid
  - key





## 2.反编译【失败】

![image-20220419171632575](assets/image-20220419171632575.png)



## 3.脱壳

使用 **armpro** 可以帮助你快速实现脱壳（不是所有的都能脱）。



### 3.1 安装 armpro

本节课件目录下有 armpro 的安装包【Arm Pro_1.3.1.apk】，自行下载并安装到自己手机。**（需购买会员）**

<img src="assets/image-20220419172202209.png" alt="image-20220419172202209" style="zoom: 50%;" />

### 3.2 脱壳

![image-20220419172948444](assets/image-20220419172948444.png)

![image-20220419173435422](assets/image-20220419173435422.png)



### 3.3 mt管理器

在手机上安装 mt 管理器，对脱壳出来的文件进行修复。

本节课件目录下有 armpro 的安装包【MT2.10.4.apk】，自行下载并安装到自己手机。**（需购买会员）**

<img src="assets/image-20220419174109909.png" alt="image-20220419174109909" style="zoom: 50%;" />



#### 3.3.1 解压

![image-20220419174644915](assets/image-20220419174644915.png)

![image-20220419175009564](assets/image-20220419175009564.png)



#### 3.3.2 删除dex

检查dex文件，把加固的dex删除掉。

![image-20220419175201985](assets/image-20220419175201985.png)

![image-20220419175634506](assets/image-20220419175634506.png)



#### 3.3.3 重命名

![image-20220419180135590](assets/image-20220419180135590.png)

![image-20220419180412914](assets/image-20220419180412914.png)

#### 3.3.4 修复

![image-20220419180658221](assets/image-20220419180658221.png)



#### 3.3.5 移动至apk

把上述修复完的dex文件，移动到apk文件中。

![image-20220419181947499](assets/image-20220419181947499.png)

![image-20220419182206958](assets/image-20220419182206958.png)

![image-20220419182331784](assets/image-20220419182331784.png)

注意：此apk文件包含了所有代码，可以对他进行反编译，但无法安装运行在你的手机上，如果想要修改并运行到手机上，还需要对原apk文件进行 去除签名 & 重新签名。



### 3.4 反编译

![image-20220419181605975](assets/image-20220419181605975.png)

![image-20220419181634637](assets/image-20220419181634637.png)









目前当前app文件：

- 手机：安装原版app文件
- 电脑：jadx反编译，脱壳的apk文件。



## 4.发送短信

![image-20220419184430907](assets/image-20220419184430907.png)



### 4.1 sign

sign的值是什么？

```python
import hashlib
import time

# 模拟校验
phone = "18630087660"
timestamp = int(time.time())  # 1649503254306
ending = "@SMS_MEMBER" if timestamp % 2 else "@SMS_TIANGOU"
data_string = f"{phone}{timestamp}{ending}"

ha = hashlib.md5()
ha.update(data_string.encode('utf-8'))
sign = ha.hexdigest()

# 正确
print(sign)  # 3215e58cfbb890b5737ed6bf6fc2c401
```



### 4.2 请求头

![image-20220419185400325](assets/image-20220419185400325.png)

![image-20220419185534739](assets/image-20220419185534739.png)



#### 4.2.1 tgs_uuid

![image-20220419185627461](assets/image-20220419185627461.png)

![image-20220419185607425](assets/image-20220419185607425.png)



#### 4.2.2 key

![image-20220419185736524](assets/image-20220419185736524.png)





### 4.3 整合（发短信）

```python
import requests
import hashlib
import time
import uuid

def md5(arg):
    ha = hashlib.md5()
    ha.update(arg.encode('utf-8'))
    return ha.hexdigest()

# 1.sign签名
phone = "手机号"
timestamp = int(time.time()*1000)  # 1649503254306
ending = "@SMS_MEMBER" if timestamp % 2 else "@SMS_TIANGOU"
data_string = f"{phone}{timestamp}{ending}"
sign = md5(data_string)

# 2.key
version = "tgou_Android_V2.6.28"
data_string = f"{version}miyue"
key = md5(data_string)
print(key)

# 3.tags_uuid
tgs_uuid = str(uuid.uuid4()) 

res = requests.post(
    url="https://mServ.51tiangou.com/publics/sms/sendVerificationCodeForApp",
    data={
        "sign": sign,
        "cellphone": phone,
        "type": "21",
        "voiceType": "0",
        "timestamp": timestamp
    },
    headers={
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Redmi 8A MIUI/V12.5.3.0.QCPCNXM)@tiangou/android/20210427/1649503254313",
        # "deviceId": "020000000000",
        "version": "tgou_Android_V2.6.28",
        "tgVersion": "@tiangou/android/20210427/1649503254313",
        "mid_version": "8",
        "mid_global": "android",
        "key": key,
        "tgs_uuid": tgs_uuid,
        "Host": "mServ.51tiangou.com",
    }
)

print(res.text)
```



注意：现在不行（app不支持功能）。



## 5.注册

![image-20220419190543996](assets/image-20220419190543996.png)

![image-20220419190605333](assets/image-20220419190605333.png)



![image-20220419190753713](assets/image-20220419190753713.png)

```
[
    "BsUXUZD9xt8+M4Ew4Fa132sEcrELuz1LqWR8JESfbljcB94tdRpsmiW3bA=",
    "H/X+yJfosTFGvoKLTvQ06rlWbk1LO+ESMgshuwxwrK8E2yoNKbZynMI3XQc4=",
    "tdDqOqpuCgd1BqVS8HPXcrTB/4nX23vk6PRlNb9RxXQXwIclmX4xIYLq64+4=",
    "jQ0yXbTajPfsPnhrUPMzn+YsPPf8j/qquUXMdq/2yrqxij2MaWuWU3UYpcNEO2HY=",
    "FvBm+jv4icSphn7D/75Ut5u9tXeXcDSzuQ64RamaZpavH9P+szaKM8=",
    "Gsi1XNi3aU8V+cGdCJ9OYvoNjNsXUaemNZXD8rpGmezEAuiadgFICABw9LRg="
]
```



### 5.1 一通乱找

一通乱搜和hook，包括：RSA、AES、sha1加密都找了，都不是。

![image-20220419191707892](assets/image-20220419191707892.png)



加密都会执行：

```
 KeyFactory instance = KeyFactory.getInstance(str);
```

hook他就发现：

```python
import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("com.dashang.tiangou")

scr = """
Java.perform(function () {
    var RSAUtil = Java.use("com.dashang.tiangou.cloudpayment.a.d");
    var KeyFactory = Java.use("java.security.KeyFactory");
    var h = Java.use("com.kh.keyboard.h");
    
    KeyFactory.getInstance.overload('java.lang.String').implementation = function(i){
        console.log("来了",i);
        // console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
        return this.getInstance(i);
    }
    
});
"""
script = session.create_script(scr)


def on_message(message, data):
    print(message)


script.on("message", on_message)
script.load()
sys.stdin.read()

```

发现每次输入一个字符，都会触发一下 ----> 每次输入都会加密。



获取他的调用栈：

![image-20220409223110760](assets/image-20220409223110760.png)



继续hook里面的a方法：

```python
import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("com.dashang.tiangou")

scr = """
Java.perform(function () {
    var RSAUtil = Java.use("com.dashang.tiangou.cloudpayment.a.d");
    var KeyFactory = Java.use("java.security.KeyFactory");
    var h = Java.use("com.kh.keyboard.h");
    
    KeyFactory.getInstance.overload('java.lang.String').implementation = function(i){
        console.log("来了",i);
        // console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
        return this.getInstance(i);
    }
    
    h.a.overload('java.lang.String', 'java.lang.String', 'java.lang.String').implementation = function(str,str2,str3){
        console.log("str=",str);
        console.log("str2=",str2);
        console.log("str3=",str3);
        var res = this.a(str,str2,str3);
        console.log("结果=",res);
        console.log("-----------------------");
        return res;
    }
    
});
"""
script = session.create_script(scr)


def on_message(message, data):
    print(message)


script.on("message", on_message)
script.load()
sys.stdin.read()
```



输出：

```
str=1
str2= MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9G4LU8LZtxApKhP81Usk7ze7obk8osQQcHhVdEfVoVIL3PTd2oIknWBBdIQz/r7HCVeZr6kMaESFc6dpmLime06JWyg902I0S+e8UnAaXhIQJso4wBVD4KtRKozCZ4XzFg8xK40/jO3rJA7WU7Tsn2qcr+MYyqLnN31umo3zZZwIDAQAB
str3= UTF-8
来了 RSA
结果= BsUXUZD9xt8+M4Ew4Fa132sEcrELuz1LqWR8JESfbljciXlOvvCXT/BCVnempGtaw63q9dQwMOqk2BOb03AaxvHuet2xFieVe6RBWvHcas1NwYMEiJyejq3RlZcXyvc7ntg6g7s7MPiIV8fE4H3d6jEACoj4aB94tdRpsmiW3bA=
-----------------------
str= 2
str2= MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9G4LU8LZtxApKhP81Usk7ze7obk8osQQcHhVdEfVoVIL3PTd2oIknWBBdIQz/r7HCVeZr6kMaESFc6dpmLime06JWyg902I0S+e8UnAaXhIQJso4wBVD4KtRKozCZ4XzFg8xK40/jO3rJA7WU7Tsn2qcr+MYyqLnN31umo3zZZwIDAQAB
str3= UTF-8
来了 RSA
结果= H/X+yJfosTFGvoKLTvQ06rlWbk1LO+ESMgshuwxwrK8ARxPidXd8QuawRmuWP+iK4/e5I44nSgSVVEFPYROIS12Nz2Uxefe0A5MG0d1LtN1eTjp+lKuJXbWMlNHS6Sr0zBetYJL6yvCxSOBRUgOtTtev9eE2yoNKbZynMI3XQc4=
-----------------------
str= 3
str2= MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9G4LU8LZtxApKhP81Usk7ze7obk8osQQcHhVdEfVoVIL3PTd2oIknWBBdIQz/r7HCVeZr6kMaESFc6dpmLime06JWyg902I0S+e8UnAaXhIQJso4wBVD4KtRKozCZ4XzFg8xK40/jO3rJA7WU7Tsn2qcr+MYyqLnN31umo3zZZwIDAQAB
str3= UTF-8
来了 RSA
结果= tdDqOqpuCgd1BqVS8HPXcrTB/4nX23vk6PRlNb9RxXQXwIcmxHjapA7nHzLW4NLlu+UygdSBWM+d964UK4//7EPCGZj/BiaezzbdpIetJyoV2sXJWV4+kzbhOtLZWs98TeIo4HPFwM+tsuW00MOiSgN9aiO3R6lmX4xIYLq64+4=
-----------------------
str= q
str2= MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9G4LU8LZtxApKhP81Usk7ze7obk8osQQcHhVdEfVoVIL3PTd2oIknWBBdIQz/r7HCVeZr6kMaESFc6dpmLime06JWyg902I0S+e8UnAaXhIQJso4wBVD4KtRKozCZ4XzFg8xK40/jO3rJA7WU7Tsn2qcr+MYyqLnN31umo3zZZwIDAQAB
str3= UTF-8
来了 RSA
结果= jQ0yXbTajPfsPnhrUPMzn+YsPPf8SOnWkuyeYg2SpoceWNwxSLxIiLlzrdBEIiok47L25QwCgSmg7bNbGjSKCFCKORl8FzeBQ7c7mnHbi4WVAjgNe7sNDmMJUsdb3sKC/KvZU48j/qquUXMdq/2yrqxij2MaWuWU3UYpcNEO2HY=
-----------------------
str= w
str2= MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9G4LU8LZtxApKhP81Usk7ze7obk8osQQcHhVdEfVoVIL3PTd2oIknWBBdIQz/r7HCVeZr6kMaESFc6dpmLime06JWyg902I0S+e8UnAaXhIQJso4wBVD4KtRKozCZ4XzFg8xK40/jO3rJA7WU7Tsn2qcr+MYyqLnN31umo3zZZwIDAQAB
str3= UTF-8
来了 RSA
结果= FvBm+jv4icSphn7D/75Ut5u9tXffku+1KXRQ7sgTdYKjzSfQPSLpWuO4rr3f8466teUkVN9OTFlu6Zq+eTysZDzTcwguSQHc/YFMQpITHnV7TCc7kdE7B4EUGPJPZDoBlFn134DSBJ6CrTVeXcDSzuQ64RamaZpavH9P+szaKM8=
-----------------------
str= e
str2= MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9G4LU8LZtxApKhP81Usk7ze7obk8osQQcHhVdEfVoVIL3PTd2oIknWBBdIQz/r7HCVeZr6kMaESFc6dpmLime06JWyg902I0S+e8UnAaXhIQJso4wBVD4KtRKozCZ4XzFg8xK40/jO3rJA7WU7Tsn2qcr+MYyqLnN31umo3zZZwIDAQAB
str3= UTF-8
来了 RSA
结果= Gsi1XNi3aU8V+cGdCJ9OYvoNjNsXUaemNZ/cfUjTLymDKhFuB4h3bh5eNimGAikodgCsgwbgebdrKZJV35rAX/gWX80NwgP7CEpsjQeanH+lGJqyYv/dQENYT82aRV1HqOxJ57Id/R8USISu7XD8rpGmezEAuiadgFICABw9LRg=
-----------------------
```





### 5.2 正经过程

![image-20220419191256377](assets/image-20220419191256377.png)



![image-20220419191412276](assets/image-20220419191412276.png)



```python
import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("com.dashang.tiangou")

scr = """
Java.perform(function () {
    var RSAUtil = Java.use("com.dashang.tiangou.cloudpayment.a.d");
    var KeyFactory = Java.use("java.security.KeyFactory");
    var h = Java.use("com.kh.keyboard.h");
    
    KeyFactory.getInstance.overload('java.lang.String').implementation = function(i){
        console.log("来了",i);
        // console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
        return this.getInstance(i);
    }
    
    h.a.overload('java.lang.String', 'java.lang.String', 'java.lang.String').implementation = function(str,str2,str3){
        console.log("str=",str);
        console.log("str2=",str2);
        console.log("str3=",str3);
        var res = this.a(str,str2,str3);
        console.log("结果=",res);
        console.log("-----------------------");
        return res;
    }
    
});
"""
script = session.create_script(scr)


def on_message(message, data):
    print(message)


script.on("message", on_message)
script.load()
sys.stdin.read()
```





### 5.3 密码的生成

```
import org.apache.commons.net.util.C11663a;
这玩意就是base64加密
```

![image-20220410001502765](assets/image-20220410001502765.png)

```java
"""
    pip install rsa
"""
    
import rsa
import base64


def encrypt_password(data_string):
    data_list = []
    for char in data_string:
        pub_key_str = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9G4LU8LZtxApKhP81Usk7ze7obk8osQQcHhVdEfVoVIL3PTd2oIknWBBdIQz/r7HCVeZr6kMaESFc6dpmLime06JWyg902I0S+e8UnAaXhIQJso4wBVD4KtRKozCZ4XzFg8xK40/jO3rJA7WU7Tsn2qcr+MYyqLnN31umo3zZZwIDAQAB\n-----END PUBLIC KEY-----\n'
        key = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key_str.encode('utf-8'))
        rsa_bytes = rsa.encrypt(char.encode(encoding='utf-8'), key)
        b64_bytes = base64.b64encode(rsa_bytes)
        data_list.append(b64_bytes.decode('utf-8'))
    return data_list


password = encrypt_password("wupeiqi")
print(password)
```



### 5.4 整合（注册）

```python
import uuid
import json
import hashlib
import base64

import rsa
import requests


def md5(arg):
    ha = hashlib.md5()
    ha.update(arg.encode('utf-8'))
    return ha.hexdigest()


def encrypt_password(data_string):
    data_list = []
    for char in data_string:
        pub_key_str = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9G4LU8LZtxApKhP81Usk7ze7obk8osQQcHhVdEfVoVIL3PTd2oIknWBBdIQz/r7HCVeZr6kMaESFc6dpmLime06JWyg902I0S+e8UnAaXhIQJso4wBVD4KtRKozCZ4XzFg8xK40/jO3rJA7WU7Tsn2qcr+MYyqLnN31umo3zZZwIDAQAB\n-----END PUBLIC KEY-----\n'
        key = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key_str.encode('utf-8'))
        rsa_bytes = rsa.encrypt(char.encode(encoding='utf-8'), key)
        b64_bytes = base64.b64encode(rsa_bytes)
        data_list.append(b64_bytes.decode('utf-8'))
    pwd_string = json.dumps(data_list)
    return pwd_string


# 2.key
version = "tgou_Android_V2.6.28"
data_string = f"{version}miyue"
key = md5(data_string)

# 3.tags_uuid
tgs_uuid = str(uuid.uuid4())  # "eacb9c3d-65b9-4a33-bcd9-9df194a4f913",  # uuid，请求刚加载，放在xml中

res = requests.post(
    url="https://mServ.51tiangou.com/publics/register/appRegister",
    data={
        "password": encrypt_password("qwe123qwe"),
        "code": "1111",
        "defaultCityId": "2554",
        "sourceType": 4,
        "cellPhone": "136302187666",
    },
    headers={
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Redmi 8A MIUI/V12.5.3.0.QCPCNXM)@tiangou/android/20210427/1649503254313",
        "version": "tgou_Android_V2.6.28",
        "tgVersion": "@tiangou/android/20210427/1649503254313",
        "mid_version": "8",
        "mid_global": "android",
        "key": key,
        "tgs_uuid": tgs_uuid,
        "Host": "mServ.51tiangou.com",
    }
)

print(res.text)
```





## 6.完整版（短信+注册）

```python
import time
import uuid
import json
import hashlib
import base64

import rsa
import requests


def md5(arg):
    ha = hashlib.md5()
    ha.update(arg.encode('utf-8'))
    return ha.hexdigest()


def encrypt_password(data_string):
    data_list = []
    for char in data_string:
        pub_key_str = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC9G4LU8LZtxApKhP81Usk7ze7obk8osQQcHhVdEfVoVIL3PTd2oIknWBBdIQz/r7HCVeZr6kMaESFc6dpmLime06JWyg902I0S+e8UnAaXhIQJso4wBVD4KtRKozCZ4XzFg8xK40/jO3rJA7WU7Tsn2qcr+MYyqLnN31umo3zZZwIDAQAB\n-----END PUBLIC KEY-----\n'
        key = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key_str.encode('utf-8'))
        rsa_bytes = rsa.encrypt(char.encode(encoding='utf-8'), key)
        b64_bytes = base64.b64encode(rsa_bytes)
        data_list.append(b64_bytes.decode('utf-8'))
    pwd_string = json.dumps(data_list)
    return pwd_string


def send_sms(phone, version, key, tgs_uuid):
    # 1.sign签名
    timestamp = int(time.time() * 1000)  # 1649503254306
    ending = "@SMS_MEMBER" if timestamp % 2 else "@SMS_TIANGOU"
    data_string = f"{phone}{timestamp}{ending}"
    sign = md5(data_string)

    res = requests.post(
        url="https://mServ.51tiangou.com/publics/sms/sendVerificationCodeForApp",
        data={
            "sign": sign,
            "cellphone": phone,
            "type": "21",
            "voiceType": "0",
            "timestamp": timestamp
        },
        headers={
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Redmi 8A MIUI/V12.5.3.0.QCPCNXM)@tiangou/android/20210427/1649503254313",
            "version": version,
            "tgVersion": "@tiangou/android/20210427/1649503254313",
            "mid_version": "8",
            "mid_global": "android",
            "key": key,
            "tgs_uuid": tgs_uuid,
            "Host": "mServ.51tiangou.com",
        }
    )

    print(res.text)


def register(phone, password, code, version, key, tgs_uuid):
    res = requests.post(
        url="https://mServ.51tiangou.com/publics/register/appRegister",
        data={
            "password": encrypt_password(password),
            "code": code,
            "defaultCityId": "2554",
            "sourceType": 4,
            "cellPhone": phone,
        },
        headers={
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Redmi 8A MIUI/V12.5.3.0.QCPCNXM)@tiangou/android/20210427/1649503254313",
            "version": version,
            "tgVersion": "@tiangou/android/20210427/1649503254313",
            "mid_version": "8",
            "mid_global": "android",
            "key": key,
            "tgs_uuid": tgs_uuid,
            "Host": "mServ.51tiangou.com",
        }
    )

    print(res.text)


def run():
    phone = "17531111111"
    password = "qwe123qwe"

    # 请求头：version
    version = "tgou_Android_V2.6.28"

    # 请求头：key
    data_string = f"{version}miyue"
    key = md5(data_string)

    # 请求头：tags_uuid
    tgs_uuid = str(uuid.uuid4())  # "eacb9c3d-65b9-4a33-bcd9-9df194a4f913",  # uuid，请求刚加载，放在xml中

    # 发送短信
    send_sms(phone, version, key, tgs_uuid)

    # 短信验证码
    code = input(">>>")

    # 注册
    register(phone, password, code, version, key, tgs_uuid)


if __name__ == '__main__':
    run()
```



## 7.扩展

- 注册
- 登录





## 最后一天

- 小红书

- 学爬虫的目的：搞钱

  - 1~5w，以内的项目。

    ```
    1~2w，项目（信息差）
    
    dex文件结构、android系统dex文件加载、工具 -> 脱壳
    so，汇编、arm、二进制、frdia
    ```

  - 5w ~ 100w，项目

    ```
    1人 vs  公司（经改变、风控）
    ```

- 圈子（谁把我灌醉）























































































































