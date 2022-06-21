python判断的开头结尾有快捷方法如下：

1、判断开头：　

```python
string.startswith("目标字符")
```

2、判断结尾：

```
string.endswith("目标字符")
```

返回 

```
True  or  False
```

另，提示一点，判断之前请先去除字符串首尾空格，方法：

```
string.strip()
```