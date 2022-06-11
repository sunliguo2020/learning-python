# day05 初识app逆向

关于逆向知识：

- JS逆向案例，通过分析JS代码，得到算法，Python实现出来。

  ```
  必备技能：JavaScript编程语言、DOM、BOM、Chrome工具（抓包、调试）、经验（猜想、尝试）。
  ```

- app逆向，抓包+分析app中的代码，得到内部算法，Python代码伪造出来。



**今日目标：**

- 臧航准备网
- 油联合伙人



## 1.臧航准备网





### 1.1 设备

- 安卓手机，大家务必人手一部 + **必须root** 【暂时不需要，大概day10】

  ```
  手机root的步骤：
  	- 解BL锁（官方申请，注意：切记不要重复申请，大致7天）
  	- 刷REC再刷面具进行ROOT
  注意：淘宝、咸鱼。
  ```

- 模拟器，在电脑上模拟出一部手机。

  ```
  win: 逍遥、夜神、雷电、网易mumu等。
  mac: 网易mumu （暂时不支持m1）
  
  win系统同学，开启VT：https://mumu.163.com/include/16v1/2016/06/27/21967_625825.html
  m1的同学，搞一部真机+root。
  ```

  

当你安装好模拟器之后，要开启root权限。

![image-20220125202321810](assets/image-20220125202321810.png)



### 1.2 安装app

![image-20220125203204717](assets/image-20220125203204717.png)

![image-20220125203154220](assets/image-20220125203154220.png)



<img src="assets/image-20220125203327791.png" alt="image-20220125203327791" style="zoom:25%;" />





### 1.3 抓包软件 charles

抓包软件的思路：

- 设备 + PC 在同一个网络。
- PC：安装抓包软件。
- 设备：配置，设备想要发送网络请求都是由PC软件进行转发。



#### 1.3.1 安装charles

- mac用户

  ```
  访问网址 https://xclient.info/s/charles.html 根据提示下载并破解。
  ```

- windows用户：

  ```
  下载地址：（ charles v4.5.6，大家也可去网上自行下载和破解 ）
  	链接: https://pan.baidu.com/s/1gedTGrFsB1SnNwTvPLoZPg 提取码: cjfe 
  	
  注册码
  	Registered Name:  https://zhile.io
  	License Key:      48891cf209c6d32bf4
  ```



#### 1.3.2 Http配置

##### 1.3.1 PC

打开 【Proxy】>【Proxy Settings】设置代理IP端口：

![image-20220125204046033](assets/image-20220125204046033.png)



查看charles所在的PC的IP地址：

![image-20220125204152266](assets/image-20220125204152266.png)



##### 1.3.2 设备

让设备用PC上的charles做请求的代理。

![image-20220125204335039](assets/image-20220125204335039.png)





至此，就可以基于charles来抓包了。但是他只能抓取http的请求包。

```
http://www.xxx.com/....    -> 明文
https://www.xxx.com/....   -> 密文
```





#### 1.3.3 Https配置

本质就需要安装证书（charles生成一个证书、安装到设备中）。

- andrioid7以下，直接安装证书即可。【mumu 的 android 6.0.1】
- andrioid7及以上，root + 安装成系统证书。



##### 1.3.1 PC

打开 【Proxy】>【SSL Proxying Settings】开启HTTPS：

![image-20220125162645707](assets/image-20220125162645707.png)

![image-20220125175825959](assets/image-20220125175825959.png)





在设备上安装证书之前，需要在charles中打开安装界面，查看流程：



![image-20210928175031248](../../../../路飞工作/第二期 爬虫和APP逆向课程/day05 初识app逆向/assets/image-20210928175031248.png)

![image-20210928175103171](../../../../路飞工作/第二期 爬虫和APP逆向课程/day05 初识app逆向/assets/image-20210928175103171.png)





##### 1.3.2 设备



> android7 以下版本可用。





![image-20210928175216018](assets/image-20210928175216018.png)

![image-20210928175243620](assets/image-20210928175243620.png)

![image-20220125175956217](assets/image-20220125175956217.png)

安装成功后，就可以在charles中进行抓包了。



至此，抓包软件的配置完成（http/https）。



### 1.4 案例

抓取登录的请求包，然后进行分析。

![image-20220125210753900](assets/image-20220125210753900.png)

```python
import requests

res = requests.post(
    url="http://cd.tibetairlines.com.cn:9100/login",
    data={
        "grant_type": "password",
        "isLogin": True,
        "password": 'sb123',
        "username": 'alex,C',
    }
)

print(res.text)
```



## 2.油联合伙人

逆向登录中的算法。



### 2.1 安装app

下载并安装软件。

- 豌豆荚下载地址：https://www.wandoujia.com/apps/8051276
- 百度网盘：课件目录（其他资料包）。



### 2.2 抓包

![image-20220125211650717](assets/image-20220125211650717.png)



```
URL
	https://chinayltx.com/app/api/v1/partnerLogin/login
请求体
	                           123123123
	phone=18988812345&password=f5bb0c8de146c67b44babbf4e6584cc0

请求头
	X-App: native
    X-Noncestr: 123456
    X-OS: partnerApp_android
    X-Req-Time: 1643116574398
    X-Sign: 8f931adf3cdd70f683e01f293c870105
    X-Token: 
    X-UserID: 
```



接下来，我们就应去app的源码中找咱们相关的算法。

```
安卓的应用 + Java代码来编写 => 编译  apk文件。
```



### 2.3 反编译

将apk文件反编译成java代码 + 分析java代码。



今日我们用的反编译工具：JEB、GDA、**JADX**。（依赖JRE) 



#### 2.3.1 安装JDK

需要在你的电脑上安装Java开发工具包JDK，JDK中包含JRE。

```
https://www.oracle.com/java/technologies/downloads/

# 推荐：JDK8==JDK1.8（后期工具需要）
https://www.oracle.com/java/technologies/downloads/#java8
```



安装好之后需要配置下环境变量。

![image-20210929163956511](assets/image-20210929163956511.png)



![image-20210929163410661](assets/image-20210929163410661.png)





关于mac系统，自带JDK：

![image-20210929152514354](assets/image-20210929152514354.png)

```
/Library/Java/JavaVirtualMachines 
```

![image-20210929152444076](assets/image-20210929152444076.png)



#### 2.3.2 jadx

直接解压。

注意：代码、文件尽量不要让他存在中文路径。





![image-20210928184518710](assets/image-20210928184518710.png)

![image-20220125183725576](assets/image-20220125183725576.png)



### 2.4 去源码中寻找算法

```
URL
	https://chinayltx.com/app/api/v1/partnerLogin/login
请求体
	                           123123123
	phone=18988812345&password=f5bb0c8de146c67b44babbf4e6584cc0
	
	

请求头
	X-App: native
    X-Noncestr: 123456
    X-OS: partnerApp_android
    X-Req-Time: 1643116574398
    X-Sign: 8f931adf3cdd70f683e01f293c870105
    X-Token: 
    X-UserID: 
```

- 密码如何加密
- X-Sign如何加密



#### 2.4.1 密码逆向

- 搜：password、"password"、password=、password=f5bb0c8de146c67b44babbf4e6584cc0
- 搜：phone
- 搜：url



![image-20220125214814454](assets/image-20220125214814454.png)



![image-20220125215154461](assets/image-20220125215154461.png)

下一步搜索，谁使用了submitLogin。

loginWithToken(值1，值2)





![image-20220125220041629](assets/image-20220125220041629.png)



![image-20220125220108562](assets/image-20220125220108562.png)

![image-20220125220129233](assets/image-20220125220129233.png)



我们找到了“可能”是这个MD5加密。

- 可能是错误的Hook框架验证（后期）

- 猜想。

  ```
  123123123
  f5bb0c8de146c67b44babbf4e6584cc0
  ```

  ```python
  import hashlib
  
  obj = hashlib.md5()
  obj.update("123123123".encode('utf-8'))
  res = obj.hexdigest()
  print(res)
  
  # f5bb0c8de146c67b44babbf4e6584cc0
  ```



#### 2.4.2 X-Sign逆向

```
URL
	https://chinayltx.com/app/api/v1/partnerLogin/login
请求体
	                           123123123
	phone=18988812345&password=f5bb0c8de146c67b44babbf4e6584cc0
	
	

请求头
	X-App: native
    X-Noncestr: 123456
    X-OS: partnerApp_android
    X-Req-Time: 1643116574398
    X-Sign: 8f931adf3cdd70f683e01f293c870105
    X-Token: 
    X-UserID: 
```



搜索：X-Sign



![image-20220125221155325](assets/image-20220125221155325.png)



![image-20220125222310620](assets/image-20220125222310620.png)

```python
import hashlib


token = ""
reqTime = "1643116574398"
nonce_str = "123456"
nonce_str_sub_2 = nonce_str[2:]
body_string = "phone=18988812345&password=f5bb0c8de146c67b44babbf4e6584cc0"

encrypt_string = f"{token}{reqTime}{nonce_str_sub_2}{body_string}"



obj = hashlib.md5()
obj.update(encrypt_string.encode('utf-8'))
res = obj.hexdigest()
print(res)

# 8f931adf3cdd70f683e01f293c870105
# 8f931adf3cdd70f683e01f293c870105
```









## 总结

- 设备：真机 + 模拟器
- 抓包：
  - http
  - https
- 反编译apk
  - jre -> JDK包含jre
  - jadx
  - 根据jadx反编译apk
- 逆向：搜索关键 + 分析代码 + 验证 + python实现。



大家的短板是什么？

- 看不懂 Java代码
- 看不懂 安卓开发+常用的包





























