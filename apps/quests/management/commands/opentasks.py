# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

from django.core.management import BaseCommand
from operator import itemgetter
import operator
from optparse import make_option
from quests.models import Quest
from teams.models import Team

__author__ = 'Last G'


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-c', '--categories',
                    action='append',
                    type='string',
                    dest='categories',
                    default=[],
                    help='Only in this categories'),
        make_option('-s', '--score',
                    action='store',
                    type='int',
                    dest='score',
                    default=False,
                    help='All tasks with score less than'),
        make_option('-o', '--opened_by_someone',
                    action='store_true',
                    default=False,
                    dest='by_someone',
                    help='Opens tasks only opened to someone'),
    )

    def handle(self, *args, **options):
        quests = Quest.objects.all().order_by('shortname')
        teams = list(Team.objects.all())

        filters = dict()

        if options['categories']:
            filters['category__name__in'] = options['categories']
        if options['score']:
            filters['score__lte'] = options['score']
        if options['by_someone']:
#            teams_ids = map(operator.attrgetter('id'), teams)
            filters['open_for__in'] = teams

        quests = quests.filter(**filters).distinct()
        num = 0
        for num, q in enumerate(quests):
            print("Opening quest: {}".format(q.shortname))
            q.open_for.add(*teams)
            q.save()
        print("Total updated: {}".format(num))