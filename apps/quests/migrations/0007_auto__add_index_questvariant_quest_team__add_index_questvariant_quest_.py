# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'QuestVariant', fields ['quest', 'team']
        db.create_index('quests_questvariant', ['quest_id', 'team_id'])

        # Adding index on 'QuestVariant', fields ['quest', 'team', 'is_valid', 'timeout']
        db.create_index('quests_questvariant', ['quest_id', 'team_id', 'is_valid', 'timeout'])

        # Adding index on 'QuestAnswer', fields ['quest_variant', 'is_success', 'is_checked']
        db.create_index('quests_questanswer', ['quest_variant_id', 'is_success', 'is_checked'])

        # Adding index on 'QuestAnswer', fields ['is_success', 'is_checked']
        db.create_index('quests_questanswer', ['is_success', 'is_checked'])


    def backwards(self, orm):
        # Removing index on 'QuestAnswer', fields ['is_success', 'is_checked']
        db.delete_index('quests_questanswer', ['is_success', 'is_checked'])

        # Removing index on 'QuestAnswer', fields ['quest_variant', 'is_success', 'is_checked']
        db.delete_index('quests_questanswer', ['quest_variant_id', 'is_success', 'is_checked'])

        # Removing index on 'QuestVariant', fields ['quest', 'team', 'is_valid', 'timeout']
        db.delete_index('quests_questvariant', ['quest_id', 'team_id', 'is_valid', 'timeout'])

        # Removing index on 'QuestVariant', fields ['quest', 'team']
        db.delete_index('quests_questvariant', ['quest_id', 'team_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'quests.category': {
            'Meta': {'object_name': 'Category'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_index': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'db_index': 'True'})
        },
        'quests.quest': {
            'Meta': {'object_name': 'Quest', 'ordering': "['-score']"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quests.Category']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_manual': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_simple': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'open_for': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['teams.Team']", 'symmetrical': 'False', 'blank': 'True'}),
            'provider_file': ('django.db.models.fields.FilePathField', [], {'max_length': '100', 'path': "'D:\\\\Workspace\\\\GitHub\\\\qoala\\\\data\\\\tasks'", 'db_index': 'True', 'recursive': 'True'}),
            'provider_hash': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'provider_state': ('django.db.models.fields.BinaryField', [], {'null': 'True'}),
            'provider_type': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_index': 'True', 'unique': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'db_index': 'True'})
        },
        'quests.questanswer': {
            'Meta': {'object_name': 'QuestAnswer', 'index_together': "[['is_success', 'is_checked'], ['quest_variant', 'is_success', 'is_checked']]"},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'answer_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_checked': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_success': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'quest_variant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quests.QuestVariant']"}),
            'result': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'db_index': 'True'})
        },
        'quests.questvariant': {
            'Meta': {'object_name': 'QuestVariant', 'index_together': "[['quest', 'team'], ['quest', 'team', 'is_valid', 'timeout']]"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_valid': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'quest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quests.Quest']"}),
            'state': ('django.db.models.fields.BinaryField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['teams.Team']"}),
            'timeout': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'try_count': ('django.db.models.fields.IntegerField', [], {'default': '1', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True', 'db_index': 'True'})
        },
        'teams.team': {
            'Meta': {'object_name': 'Team'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'db_index': 'True', 'unique': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True', 'db_index': 'True', 'null': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']"})
        }
    }

    complete_apps = ['quests']