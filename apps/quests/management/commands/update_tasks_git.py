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
                sp = subprocess.Popen(['git', 'pull'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = sp.communicate()
                self.stdout.write(stdout)
                self.stderr.write(stderr)
                if sp.returncode != 0:
                    raise CommandError("Exit code is not 0")
        except Exception as e:
            raise CommandError(str(e))
