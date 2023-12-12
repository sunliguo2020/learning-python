
在 Python 项目中，可以通过创建一个函数来设置和配置 logger，然后在整个项目中使用该函数。这种方式可以确保在项目的不同模块和文件中都使用相同的日志设置。

以下是一个示例，展示了如何在 Python 项目中创建一个函数来配置 logger：

```python
import logging

def setup_logger(logger_name, log_file, level=logging.DEBUG):
    # 创建一个 logger 实例
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # 创建一个文件处理程序
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # 创建一个格式化程序并将其应用于处理程序
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # 添加处理程序到 logger
    logger.addHandler(file_handler)

    return logger

# 例子：使用函数配置 logger
logger = setup_logger('CameraLog', 'Camera.log', level=logging.DEBUG)
```

这段代码中，`setup_logger` 函数接收了 `logger_name`、`log_file` 和 `level` 作为参数，然后配置了一个 logger，并返回了这个 logger。你可以在项目的不同模块中调用 `setup_logger` 函数，并传递相同的参数来设置相同的日志配置。



在 Python 项目中，为了保持日志配置的一致性，通常建议在项目的主入口或者设置文件中配置 logger，并且将其设置为全局的。这样，所有模块都可以使用相同的 logger 实例。

一种常见的做法是，在项目的主入口文件（例如 `main.py` 或 `app.py`）中配置 logger，并将其设置为全局变量。这样其他模块只需要导入该 logger 就可以使用了。

举例来说：

```
pythonCopy code# main.py 或 app.py

import logging

def setup_logger(logger_name, log_file, level=logging.DEBUG):
    # 创建一个 logger 实例
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # 创建一个文件处理程序
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # 创建一个格式化程序并将其应用于处理程序
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # 添加处理程序到 logger
    logger.addHandler(file_handler)

    return logger

# 配置 logger
logger = setup_logger('CameraLog', 'Camera.log', level=logging.DEBUG)
```

然后，在其他模块中导入 `logger`：

```
pythonCopy code# other_module.py

import logging

# 导入全局 logger
from main import logger

# 在模块中使用全局 logger
logger.debug("This is a debug message.")
logger.info("This is an info message.")
# ...
```

这样做可以确保在整个项目中使用相同的日志设置和配置，避免重复创建 logger 实例。






