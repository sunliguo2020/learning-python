"""
Django settings for web02_shop project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fmr5siwm-!kt%w3w#q+eehnv5et34m2m8y@bu0-$i@79d1m^i3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_filters',
    'rest_framework',
    'ckeditor',
    'users',
    'cart',
    'goods',
    'order',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 支持跨域请求
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'web02_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': []
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'web02_shop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web02_shop',
        'USER': 'root',
        'PASSWORD': 'tongmingao',
        'PORT': 3306,
        'HOST': '192.168.1.21'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 允许所有用户跨域
CORS_ORIGIN_ALL_ALL = True

# CORS_ALLOW_CREDENTIALS 指明在跨域访问中，后端是否支持对cookie的操作
CORS_ALLOW_CREDENTIALS = True

# 指定自定义用户类
AUTH_USER_MODEL = 'users.User'

# DRF的配置鉴权方式
REST_FRAMEWORK = {
    # 配置登录鉴权方式
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 配置DRF过滤器
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend',
                                "rest_framework.filters.OrderingFilter"
                                ]
}

# token的相关配置
from datetime import timedelta

SIMPLE_JWT = {
    # 访问令牌的有效时间
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=300),
    # 刷新令牌的有效时间
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    # 若为True，则刷新后新的refresh_token有更新的有效时间
    "ROTATE_REFRESH_TOKENS": False,
    # 若为True，刷新后的token将添加到黑名单
    "BLACKLIST_AFTER_ROTATION": True,
    # 对称算法：HS256 HS384 HS512 非对称:RSA
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    # if signing_key,verifying_key will be ignored.
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,

    # Authorization: Bearer <token>
    "AUTH_HEADER_TYPES": ("Bearer",),
    # if HTTP_X_ACCESS_TOKEN, X_ACCESS_TOKEN: Bearer <token>
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    # 使用唯一不变的数据库字段，将包含在生成的令牌中以标识用户
    "USER_ID_CLAIM": "user_id",
}

# 使用自定义的认证类进行身份认证（登录时验证用户信息）
AUTHENTICATION_BACKENDS = [
    'common.authentication.Authentication'
]

# 文件上传的保存路径
MEDIA_ROOT = BASE_DIR / 'file/image'
# 指定文件获取的url路径
MEDIA_URL = 'file/image/'
