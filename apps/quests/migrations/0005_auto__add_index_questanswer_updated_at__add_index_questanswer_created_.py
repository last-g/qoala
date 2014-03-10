# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'QuestAnswer', fields ['updated_at']
        db.create_index('quests_questanswer', ['updated_at'])

        # Adding index on 'QuestAnswer', fields ['created_at']
        db.create_index('quests_questanswer', ['created_at'])

        # Adding index on 'Category', fields ['updated_at']
        db.create_index('quests_category', ['updated_at'])

        # Adding index on 'Category', fields ['created_at']
        db.create_index('quests_category', ['created_at'])

        # Adding index on 'Quest', fields ['updated_at']
        db.create_index('quests_quest', ['updated_at'])

        # Adding index on 'Quest', fields ['created_at']
        db.create_index('quests_quest', ['created_at'])

        # Adding index on 'QuestVariant', fields ['updated_at']
        db.create_index('quests_questvariant', ['updated_at'])

        # Adding index on 'QuestVariant', fields ['created_at']
        db.create_index('quests_questvariant', ['created_at'])


    def backwards(self, orm):
        # Removing index on 'QuestVariant', fields ['created_at']
        db.delete_index('quests_questvariant', ['created_at'])

        # Removing index on 'QuestVariant', fields ['updated_at']
        db.delete_index('quests_questvariant', ['updated_at'])

        # Removing index on 'Quest', fields ['created_at']
        db.delete_index('quests_quest', ['created_at'])

        # Removing index on 'Quest', fields ['updated_at']
        db.delete_index('quests_quest', ['updated_at'])

        # Removing index on 'Category', fields ['created_at']
        db.delete_index('quests_category', ['created_at'])

        # Removing index on 'Category', fields ['updated_at']
        db.delete_index('quests_category', ['updated_at'])

        # Removing index on 'QuestAnswer', fields ['created_at']
        db.delete_index('quests_questanswer', ['created_at'])

        # Removing index on 'QuestAnswer', fields ['updated_at']
        db.delete_index('quests_questanswer', ['updated_at'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'quests.category': {
            'Meta': {'object_name': 'Category'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True', 'db_index': 'True'})
        },
        'quests.quest': {
            'Meta': {'ordering': "['-score']", 'object_name': 'Quest'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quests.Category']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_manual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_simple': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'open_for': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['teams.Team']", 'symmetrical': 'False'}),
            'provider_file': ('django.db.models.fields.FilePathField', [], {'recursive': 'True', 'path': "'D:\\\\Workspace\\\\GitHub\\\\qoala\\\\data\\\\tasks'", 'max_length': '100'}),
            'provider_hash': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'provider_state': ('django.db.models.fields.BinaryField', [], {'null': 'True'}),
            'provider_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'score': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'db_index': 'True', 'max_length': '60'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True', 'db_index': 'True'})
        },
        'quests.questanswer': {
            'Meta': {'object_name': 'QuestAnswer'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'answer_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_checked': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'is_success': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'quest_variant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quests.QuestVariant']"}),
            'result': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True', 'db_index': 'True'})
        },
        'quests.questvariant': {
            'Meta': {'object_name': 'QuestVariant'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'quest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quests.Quest']"}),
            'state': ('django.db.models.fields.BinaryField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"}),
            'timeout': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'try_count': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'default': '1'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True', 'db_index': 'True'})
        },
        'teams.team': {
            'Meta': {'object_name': 'Team'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'db_index': 'True', 'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'db_index': 'True', 'max_length': '60'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'null': 'True', 'db_index': 'True', 'max_length': '64'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['quests']