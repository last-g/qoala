# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import
from django.core.management import BaseCommand
from quests.models import Quest
from teams.models import Team

__author__ = 'last-g'

import logging

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Forces check of answer'

    def handle(self, *args, **options):
        teams = list(Team.objects.all())
        for quest in Quest.objects.all():
            self.stdout.write("Checking {}".format(quest.name))
            for team in teams:
                variant = quest.get_variant(team)
                if variant.last_answer and not variant.last_answer.is_checked:
                    self.stdout.write("Checking answer for {}:{} --- ".format(quest.shortname, team.name))
                    variant.last_answer.check_answer()
                    self.stdout.write("Success: {}".format(variant.last_answer.is_success))
