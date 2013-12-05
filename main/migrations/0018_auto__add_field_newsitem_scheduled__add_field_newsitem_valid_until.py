# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NewsItem.scheduled'
        db.add_column(u'main_newsitem', 'scheduled',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 18, 0, 0)),
                      keep_default=False)

        # Adding field 'NewsItem.valid_until'
        db.add_column(u'main_newsitem', 'valid_until',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 11, 18, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NewsItem.scheduled'
        db.delete_column(u'main_newsitem', 'scheduled')

        # Deleting field 'NewsItem.valid_until'
        db.delete_column(u'main_newsitem', 'valid_until')


    models = {
        u'main.file': {
            'Meta': {'object_name': 'File'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Page']"})
        },
        u'main.newsitem': {
            'Meta': {'object_name': 'NewsItem'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scheduled': ('django.db.models.fields.DateTimeField', [], {}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'valid_until': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'main.page': {
            'Meta': {'ordering': "['order']", 'object_name': 'Page'},
            'content': ('tinymce.models.HTMLField', [], {}),
            'get_pass_button': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'on_left_bar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Section']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'main.section': {
            'Meta': {'ordering': "['order']", 'object_name': 'Section'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'main.testmodel': {
            'Meta': {'ordering': "['order']", 'object_name': 'TestModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']