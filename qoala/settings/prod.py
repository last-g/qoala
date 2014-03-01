"""
This is an example settings/test.py file.
Use this settings file when running tests.
These settings overrides what's in settings/common.py
"""

from .common import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

SECRET_KEY = '_=r3oogn=z&!9m!e2l7-f(zz+y7#-+f$3b$e4rku+9&=6z!4ra'
