在Python中，`logging.basicConfig()`函数不提供直接设置日志文件编码的选项。如果你需要指定日志文件的编码为UTF-8，可以通过设置文件处理程序来实现。

```
pythonCopy codeimport logging

# 创建一个文件处理程序并设置编码为UTF-8
file_handler = logging.FileHandler(filename='Camera.log', encoding='utf-8')

# 配置日志格式和级别
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
file_handler.setLevel(logging.DEBUG)

# 获取根记录器并添加文件处理程序
root_logger = logging.getLogger()
root_logger.addHandler(file_handler)
root_logger.setLevel(logging.DEBUG)

# 示例日志记录
logging.debug('This is a test message written to the log file.')
```

此代码将创建一个文件处理程序，将其编码设置为UTF-8，并将其添加到根记录器中。你可以根据需要调整日志格式和级别。