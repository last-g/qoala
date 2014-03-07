# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Quest', fields ['shortname']
        db.create_index('quests_quest', ['shortname'])

        # Adding index on 'Quest', fields ['score']
        db.create_index('quests_quest', ['score'])

        # Adding index on 'QuestVariant', fields ['try_count']
        db.create_index('quests_questvariant', ['try_count'])

        # Adding index on 'QuestVariant', fields ['is_valid']
        db.create_index('quests_questvariant', ['is_valid'])

        # Adding index on 'QuestVariant', fields ['timeout']
        db.create_index('quests_questvariant', ['timeout'])

        # Adding index on 'QuestAnswer', fields ['score']
        db.create_index('quests_questanswer', ['score'])

        # Adding index on 'QuestAnswer', fields ['is_success']
        db.create_index('quests_questanswer', ['is_success'])

        # Adding index on 'QuestAnswer', fields ['is_checked']
        db.create_index('quests_questanswer', ['is_checked'])


    def backwards(self, orm):
        # Removing index on 'QuestAnswer', fields ['is_checked']
        db.delete_index('quests_questanswer', ['is_checked'])

        # Removing index on 'QuestAnswer', fields ['is_success']
        db.delete_index('quests_questanswer', ['is_success'])

        # Removing index on 'QuestAnswer', fields ['score']
        db.delete_index('quests_questanswer', ['score'])

        # Removing index on 'QuestVariant', fields ['timeout']
        db.delete_index('quests_questvariant', ['timeout'])

        # Removing index on 'QuestVariant', fields ['is_valid']
        db.delete_index('quests_questvariant', ['is_valid'])

        # Removing index on 'QuestVariant', fields ['try_count']
        db.delete_index('quests_questvariant', ['try_count'])

        # Removing index on 'Quest', fields ['score']
        db.delete_index('quests_quest', ['score'])

        # Removing index on 'Quest', fields ['shortname']
        db.delete_index('quests_quest', ['shortname'])


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
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
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
            'provider_file': ('django.db.models.fields.FilePathField', [], {'path': "'D:\\\\Workspace\\\\GitHub\\\\qoala\\\\data\\\\tasks'", 'recursive': 'True', 'max_length': '100'}),
            'provider_hash': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'provider_state': ('django.db.models.fields.BinaryField', [], {'null': 'True'}),
            'provider_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'score': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'db_index': 'True', 'max_length': '60'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'})
        },
        'quests.questanswer': {
            'Meta': {'object_name': 'QuestAnswer'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'answer_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_checked': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_success': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'quest_variant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quests.QuestVariant']"}),
            'result': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'})
        },
        'quests.questvariant': {
            'Meta': {'object_name': 'QuestVariant'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'quest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quests.Quest']"}),
            'state': ('django.db.models.fields.BinaryField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"}),
            'timeout': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'try_count': ('django.db.models.fields.IntegerField', [], {'default': '1', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'})
        },
        'teams.team': {
            'Meta': {'object_name': 'Team'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'db_index': 'True', 'max_length': '60'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'token': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'unique': 'True', 'null': 'True', 'max_length': '64'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']"})
        }
    }

    complete_apps = ['quests']