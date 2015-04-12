# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division, absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

from __future__ import absolute_import

from .celery import app as celery_app