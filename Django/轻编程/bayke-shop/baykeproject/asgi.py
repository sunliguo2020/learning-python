"""
<<<<<<<< HEAD:Python's Books/Django+Vue.js 实战派Python Web开发与运维/chap01/myshop-test/myshop/asgi.py
ASGI config for myshop project.
========
ASGI config for baykeproject project.
>>>>>>>> 858832e11b2d0c3d7917587feb69c7631fbc95ce:Django/轻编程/bayke-shop/baykeproject/asgi.py

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<<< HEAD:Python's Books/Django+Vue.js 实战派Python Web开发与运维/chap01/myshop-test/myshop/asgi.py
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
========
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
>>>>>>>> 858832e11b2d0c3d7917587feb69c7631fbc95ce:Django/轻编程/bayke-shop/baykeproject/asgi.py
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<<< HEAD:Python's Books/Django+Vue.js 实战派Python Web开发与运维/chap01/myshop-test/myshop/asgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'baykeproject.settings')
>>>>>>>> 858832e11b2d0c3d7917587feb69c7631fbc95ce:Django/轻编程/bayke-shop/baykeproject/asgi.py

application = get_asgi_application()
