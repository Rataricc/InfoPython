from .base import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blogDataBase',
        'USER': 'Rata',
        'PASSWORD': 'a',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}