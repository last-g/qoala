# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import
from django.core.management import BaseCommand

import csv
import sys
from pytz import timezone

from board.boards import  get_scoreboard
from quests.models import Quest
__author__ = 'last-g'

import logging

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Exports scoreboard to csv'
    can_import_settings = True

    def handle(self, *args, **options):

        fields = ['team', 'token'] + [q.name.encode('utf8') for q in Quest.objects.all()] + ['score']

        quests = list(Quest.objects.all())

        writer = csv.DictWriter(sys.stdout, fields)
        writer.writeheader()
        for team in get_scoreboard():
            row = {
                'team': team.name,
                'token': team.token,
                'score': team.score
            }
            for q in quests:
                if q.is_solved_by(team):
                    last_answer = q.get_variant(team).last_answer
                    row[q.name.encode('utf8')] = last_answer.created_at.astimezone(timezone('Asia/Yekaterinburg')).time().replace(microsecond=0)
                    if not last_answer.is_checked or not last_answer.is_success:
                        raise Exception("Last answer isn't success")
                else:
                    row[q.name.encode('utf8')] = '-'

            writer.writerow(row)


