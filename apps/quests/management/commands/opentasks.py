from django.core.management import BaseCommand
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
        )

    def handle(self, *args, **options):
        quests = Quest.objects.all()
        if options['categories']:
            quests = quests.filter(category__name__in=options['categories'])
        if options['score']:
            quests = quests.filter(score__lte=options['score'])
        teams = list(Team.objects.all())
        for q in quests:
            q.open_for.add(*teams)
            q.save()