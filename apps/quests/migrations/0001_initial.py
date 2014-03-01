# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'quests_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'quests', ['Category'])

        # Adding model 'Quest'
        db.create_table(u'quests_quest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('shortname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quests.Category'])),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('provider_type', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('provider_file', self.gf('django.db.models.fields.FilePathField')(path='/qoala/data/tasks', max_length=100, recursive=True)),
            ('provider_hash', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('is_simple', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_manual', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'quests', ['Quest'])

        # Adding M2M table for field open_for on 'Quest'
        m2m_table_name = db.shorten_name(u'quests_quest_open_for')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quest', models.ForeignKey(orm[u'quests.quest'], null=False)),
            ('team', models.ForeignKey(orm[u'teams.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['quest_id', 'team_id'])

        # Adding model 'QuestVariant'
        db.create_table(u'quests_questvariant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('quest', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quests.Quest'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Team'])),
            ('timeout', self.gf('django.db.models.fields.DateTimeField')()),
            ('try_count', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('is_valid', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('state', self.gf('django.db.models.fields.BinaryField')()),
        ))
        db.send_create_signal(u'quests', ['QuestVariant'])

        # Adding model 'QuestAnswer'
        db.create_table(u'quests_questanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('quest_variant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quests.QuestVariant'])),
            ('is_checked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_success', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('result', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('answer_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'quests', ['QuestAnswer'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'quests_category')

        # Deleting model 'Quest'
        db.delete_table(u'quests_quest')

        # Removing M2M table for field open_for on 'Quest'
        db.delete_table(db.shorten_name(u'quests_quest_open_for'))

        # Deleting model 'QuestVariant'
        db.delete_table(u'quests_questvariant')

        # Deleting model 'QuestAnswer'
        db.delete_table(u'quests_questanswer')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'quests.category': {
            'Meta': {'object_name': 'Category'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'quests.quest': {
            'Meta': {'object_name': 'Quest'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quests.Category']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_manual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_simple': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'open_for': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['teams.Team']", 'symmetrical': 'False', 'blank': 'True'}),
            'provider_file': ('django.db.models.fields.FilePathField', [], {'path': "'/qoala/data/tasks'", 'max_length': '100', 'recursive': 'True'}),
            'provider_hash': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'provider_type': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'shortname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'quests.questanswer': {
            'Meta': {'object_name': 'QuestAnswer'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'answer_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_success': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quest_variant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quests.QuestVariant']"}),
            'result': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'quests.questvariant': {
            'Meta': {'object_name': 'QuestVariant'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'quest': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quests.Quest']"}),
            'state': ('django.db.models.fields.BinaryField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Team']"}),
            'timeout': ('django.db.models.fields.DateTimeField', [], {}),
            'try_count': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'teams.team': {
            'Meta': {'object_name': 'Team'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True', 'null': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        }
    }

    complete_apps = ['quests']