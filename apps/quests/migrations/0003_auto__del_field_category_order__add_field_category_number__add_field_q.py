# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Quest.provider_state'
        db.add_column('quests_quest', 'provider_state',
                      self.gf('django.db.models.fields.BinaryField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Quest.provider_state'
        db.delete_column('quests_quest', 'provider_state')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'quests.category': {
            'Meta': {'object_name': 'Category'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'})
        },
        'quests.quest': {
            'Meta': {'object_name': 'Quest', 'ordering': "['-score']"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quests.Category']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_manual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_simple': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'open_for': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['teams.Team']", 'symmetrical': 'False'}),
            'provider_file': ('django.db.models.fields.FilePathField', [], {'recursive': 'True', 'max_length': '100', 'path': "'D:\\\\Workspace\\\\GitHub\\\\qoala\\\\data\\\\tasks'"}),
            'provider_hash': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'provider_state': ('django.db.models.fields.BinaryField', [], {'null': 'True'}),
            'provider_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'shortname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'})
        },
        'quests.questanswer': {
            'Meta': {'object_name': 'QuestAnswer'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'answer_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_success': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quest_variant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quests.QuestVariant']"}),
            'result': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'})
        },
        'quests.questvariant': {
            'Meta': {'object_name': 'QuestVariant'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'quest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quests.Quest']"}),
            'state': ('django.db.models.fields.BinaryField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"}),
            'timeout': ('django.db.models.fields.DateTimeField', [], {}),
            'try_count': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'})
        },
        'teams.team': {
            'Meta': {'object_name': 'Team'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'unique': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['quests']