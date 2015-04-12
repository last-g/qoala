# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

""" Settings for qoala """

import os

app_env = os.environ.get('APPLICATION_ENV', None)

if app_env == 'production':
    from .prod import *
elif app_env == 'test':
    from .test import *
else:
    from .dev import *