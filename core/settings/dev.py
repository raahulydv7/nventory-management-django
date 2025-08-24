from .base import *

DEBUG = True
SECRET_KEY = "django-insecure-12345abcd!@#%xyz"
ALLOWED_HOSTS = ['*']

# Development database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "inventory_db",
        "USER": "postgres",
        "PASSWORD": "root",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}