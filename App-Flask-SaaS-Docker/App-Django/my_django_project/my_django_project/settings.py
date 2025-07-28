# 2. my_django_project/settings.py

SECRET_KEY = 'fake-key-for-demo'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'myapp',
]

MIDDLEWARE = []

ROOT_URLCONF = 'my_django_project.urls'

TEMPLATES = []

WSGI_APPLICATION = 'my_django_project.wsgi.application'

STATIC_URL = '/static/'