# 启用media

1、在url.py中配置

```python
urlpatterns = [
    re_path(r'meida/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT},name='media')
]
```

2、在settins.py设置

```
MEDIA_ROOT = os.path.join(BASEDIR,'media')
MEDIA_URL = '/media/'
```

