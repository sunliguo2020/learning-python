![User](Django中统一配置logger.assets/unnamed.png)

You

在一个项目中，怎么统一配置logger？



ChatGPT

ChatGPT

在 Django 项目中，你可以使用 Django 的配置文件和 Python 的 logging 模块来统一配置 logger。以下是一个示例：

1. **在 settings.py 中设置 logger 配置**：

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'your_app_name': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # Add more loggers for other apps if needed
    },
}
```

1. **在代码中使用 logger**：

在你的 Django 应用程序中，在需要记录日志的地方，通过以下方式使用 logger：

```
import logging

logger = logging.getLogger(__name__)

def your_function():
    # 你的代码
    logger.debug('这是一个调试信息')
    logger.info('这是一个信息')
    logger.warning('这是一个警告')
    logger.error('这是一个错误')
    logger.critical('这是一个严重错误')
```

这个配置将会记录所有级别的日志信息（DEBUG、INFO、WARNING、ERROR、CRITICAL）到 `debug.log` 文件中，并且你可以在你的代码中调用 `logger` 对象记录相应级别的日志。

确保将 `'your_app_name'` 替换为你的应用程序的名称。这样配置后，在不同的地方都可以通过 `logger` 对象记录日志，且日志都会被统一记录在指定的文件中。