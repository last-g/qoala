# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import
from django.core.management import BaseCommand, CommandError
from django.conf import settings
from contextlib import contextmanager
import os
import subprocess


__author__ = 'last-g'

import logging

log = logging.getLogger(__name__)


@contextmanager
def pushd(new_dir):
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    yield
    os.chdir(previous_dir)


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        task_dir = settings.TASKS_DIR
        try:
            with pushd(task_dir):
                subprocess.check_call(['git', 'pull'], stdout=self.stdout, stderr=self.stderr)
        except Exception as e:
            raise CommandError(str(e))
