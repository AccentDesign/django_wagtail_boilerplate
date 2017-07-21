from app.settings import *


# app

INSTALLED_APPS += [
    'tests',
]

# auth

AUTH_PASSWORD_VALIDATORS = []


# files

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
