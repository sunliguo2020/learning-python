## @property和setter的用法

　　python中的@property装饰器可以总结为两个作用：

1. 让函数可以像普通变量一样使用
2. 对要读取的数据进行预处理

 **通过@property我们实现了在读取类属性前对数据进行预处理，那么我们能不能在数据从外部存入类属性前对数据进行预处理呢？** 

**@\*.setter**

　　python中的@*.setter装饰器可以总结为两个作用：

1. 对要存入的数据进行预处理
2. 设置可读属性(不可修改)

　　**注意**：@*.setter装饰器必须在@property装饰器的后面，且两个被修饰的函数的名称必须保持一致，* 即为函数名称。

```python
class User():
    def __init__(self, name):
        self.name = name
        self._password = ''   # 密文存储

    @property
    def password(self):
        return decryption(self._password)  # 解密
    @password.setter
    def password(self,word):
        self._password = encryption(word)  # 加密

user = User('xiao')
user.password = '123'   #明文输入
print(user.password)    #明文输出
```

 **总结**：为两个同名函数打上@*.setter装饰器和@property装饰器后，当把函数作为变量赋值时会触发@*.setter对应的函数，当把函数作为变量读取时会触发@property对应的函数，因此我们可以将其用于数据的预处理。 