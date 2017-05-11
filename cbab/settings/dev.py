from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(%wts-t(pgg5(%ddc66323ddse65624324=)(/&"3323v432$d8$e3x7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
