pip install chardet

chardet.detect 检查bytes格式的编码方式，不能检查字符串

```python
import chardet

a = '你好'
b = 'nihao'

a1 = a.encode()
b1 = b.encode()
print(chardet.detect(a1))
print(chardet.detect(b1))

ac = chardet.detect(a1)
print(a1.decode(ac['encoding']))
```

```python
{'encoding': 'utf-8', 'confidence': 0.7525, 'language': ''}
{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
你好

```

