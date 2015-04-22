# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import


from django.core.management import BaseCommand
from quests.models import Quest
from os.path import dirname, join, exists, isdir
from django.conf import settings
import shutil

__author__ = 'Last G'


class Command(BaseCommand):
    can_import_settings = True

    def copy_to(self, src, dst):

        if exists(dst):
            print("Removing old static files at {}".format(dst))
            shutil.rmtree(dst)

        self.stdout.write("Coping files from {} to {}".format(src, dst))
        shutil.copytree(src, dst)


    def handle(self, *args, **options):
        for task in Quest.objects.all():
            self.stdout.write("Collectiong static files for {}".format(task.shortname))
            staticdir = join(dirname(task.provider_file), 'static')
            if exists(staticdir) and isdir(staticdir):
                prefix = task.get_hashkey
                dst = join(settings.STATIC_ROOT, 'taskstatic', str(task.id), prefix)
                dst_2 = join(settings.PROJECT_DIR, 'static', 'taskstatic', str(task.id), prefix)

                for d in [dst, dst_2]:
                    try:
                        self.copy_to(staticdir, dst)
                    except Exception:
                        self.stderr.write('Could not copy from {} to {}'.format(staticdir, d))

            else:
                self.stdout.write("Have  no static files")


