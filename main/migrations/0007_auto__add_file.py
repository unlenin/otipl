# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'File'
        db.create_table(u'main_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subsection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.SubSection'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['File'])


    def backwards(self, orm):
        # Deleting model 'File'
        db.delete_table(u'main_file')


    models = {
        u'main.file': {
            'Meta': {'object_name': 'File'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subsection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.SubSection']"})
        },
        u'main.newsitem': {
            'Meta': {'object_name': 'NewsItem'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'main.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '30000'}),
            'has_news': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subsection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.SubSection']"})
        },
        u'main.section': {
            'Meta': {'ordering': "['order']", 'object_name': 'Section'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'})
        },
        u'main.subsection': {
            'Meta': {'ordering': "['order']", 'object_name': 'SubSection'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Section']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.testmodel': {
            'Meta': {'ordering': "['order']", 'object_name': 'TestModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']