from .base import *

SECRET_KEY = 'whatever'
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS + [
    'django_nose',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=webpage',
    '--cover-html'
]
