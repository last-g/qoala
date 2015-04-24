# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import
from optparse import make_option
from django.core.management import BaseCommand
from teams.models import Team

__author__ = 'last-g'

import logging

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Loads teams from file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        filename = options['filename']
        with open(filename) as f:
            user_token_pairs = [s.split() for s in f if s.strip()]
            for user, token in user_token_pairs:
                existing = Team.objects.filter(name=user, token=token).first()
                if existing:
                    self.stdout.write("Skipping {}, coz it already exists".format(user))
                else:
                    t = Team(name=user, token=token)
                    t.save()
                    self.stdout.write("Successfully created user {}".format(user))