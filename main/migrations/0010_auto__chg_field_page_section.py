# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Page.section'
        db.alter_column(u'main_page', 'section_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Section'], null=True))

    def backwards(self, orm):

        # Changing field 'Page.section'
        db.alter_column(u'main_page', 'section_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['main.Section']))

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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '30000'}),
            'has_news': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Section']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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