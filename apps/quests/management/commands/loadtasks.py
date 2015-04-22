# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from quests.models import Quest
import os
from os.path import basename

__author__ = 'Last G'

import logging
log = logging.getLogger(__name__)

class Command(BaseCommand):
    can_import_settings = True

    def load_task(self, shortname, checker_path, checker_type):
        if Quest.objects.filter(provider_file=checker_path).exists():
            quest = Quest.objects.filter(provider_file=checker_path).get()
        else:
            quest = Quest(shortname=shortname)

        quest.provider_file = checker_path
        quest.provider_type = checker_type
        quest.update_from_file(checker_type, checker_path)
        quest.save()

    def find_task(self, folder):
        pre_short = basename(folder).lower()
        for f in os.listdir(folder):
            checker_path = os.path.abspath(os.path.join(folder, f))
            fname = basename(f.lower())
            if os.path.isfile(checker_path):
                if fname == pre_short + ".xml":
                    return pre_short, checker_path, 'XMLQuestProvider'
                elif fname == pre_short:
                    return pre_short, checker_path, 'ScriptQuestProvider'

    def handle(self, *args, **options):
        for taskdir in os.listdir(settings.TASKS_DIR):
            path = os.path.join(settings.TASKS_DIR, taskdir)
            if os.path.isdir(path):
                self.stdout.write("Checking {} for task".format(path))
                res = self.find_task(path)
                if res:
                    shortname, checker, provider = res
                    self.stdout.write("Loading task {} from {}".format(shortname, checker))
                    try:
                        self.load_task(shortname, checker, provider)
                    except Exception:
                        log.exception("Could not load task %s from %s. Trying to continue", shortname, checker)
