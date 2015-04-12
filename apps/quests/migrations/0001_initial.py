# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import qtils.models
import quests.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=60, db_index=True)),
                ('number', models.IntegerField(default=quests.models.category_number, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('shortname', models.CharField(unique=True, max_length=60, db_index=True)),
                ('score', models.IntegerField(editable=False, db_index=True)),
                ('provider_type', models.CharField(max_length=60, blank=True)),
                ('provider_file', models.FilePathField(path='/opt/qoala/data/tasks', recursive=True, db_index=True)),
                ('provider_state', models.BinaryField(null=True)),
                ('provider_hash', models.CharField(max_length=60, editable=False)),
                ('is_simple', models.BooleanField(default=True, db_index=True, verbose_name='Can be checked at main thread')),
                ('is_manual', models.BooleanField(default=False, db_index=True, verbose_name='Should be checked manually')),
            ],
            options={
                'ordering': ['-score'],
            },
            bases=(qtils.models.ModelDiffMixin, models.Model),
        ),
        migrations.CreateModel(
            name='QuestAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('is_checked', models.BooleanField(default=False, db_index=True)),
                ('is_success', models.BooleanField(default=False, db_index=True)),
                ('result', models.TextField(blank=True)),
                ('score', models.IntegerField(default=0, db_index=True)),
                ('answer', models.TextField()),
                ('answer_file', models.FileField(upload_to='media', editable=False)),
            ],
            bases=(qtils.models.ModelDiffMixin, models.Model),
        ),
        migrations.CreateModel(
            name='QuestVariant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('timeout', models.DateTimeField(db_index=True)),
                ('try_count', models.IntegerField(default=1, db_index=True)),
                ('is_valid', models.BooleanField(default=True, db_index=True)),
                ('state', models.BinaryField()),
                ('quest', models.ForeignKey(to='quests.Quest')),
            ],
        ),
    ]
