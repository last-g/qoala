# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questvariant',
            name='team',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questanswer',
            name='quest_variant',
            field=models.ForeignKey(to='quests.QuestVariant'),
        ),
        migrations.AddField(
            model_name='quest',
            name='category',
            field=models.ForeignKey(editable=False, to='quests.Category'),
        ),
        migrations.AddField(
            model_name='quest',
            name='open_for',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterIndexTogether(
            name='questvariant',
            index_together=set([('quest', 'team'), ('quest', 'team', 'is_valid', 'timeout')]),
        ),
        migrations.AlterIndexTogether(
            name='questanswer',
            index_together=set([('is_success', 'is_checked'), ('quest_variant', 'is_success', 'is_checked')]),
        ),
    ]
