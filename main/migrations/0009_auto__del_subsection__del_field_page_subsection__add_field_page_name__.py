# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SubSection'
        db.delete_table(u'main_subsection')

        # Deleting field 'Page.subsection'
        db.delete_column(u'main_page', 'subsection_id')

        # Adding field 'Page.name'
        db.add_column(u'main_page', 'name',
                      self.gf('django.db.models.fields.CharField')(default='a', max_length=30),
                      keep_default=False)

        # Adding field 'Page.slug'
        db.add_column(u'main_page', 'slug',
                      self.gf('django.db.models.fields.CharField')(default='/', max_length=100),
                      keep_default=False)

        # Adding field 'Page.section'
        db.add_column(u'main_page', 'section',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['main.Section']),
                      keep_default=False)

        # Deleting field 'File.subsection'
        db.delete_column(u'main_file', 'subsection_id')

        # Adding field 'File.page'
        db.add_column(u'main_file', 'page',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['main.Page']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'SubSection'
        db.create_table(u'main_subsection', (
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Section'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['SubSection'])

        # Adding field 'Page.subsection'
        db.add_column(u'main_page', 'subsection',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['main.SubSection']),
                      keep_default=False)

        # Deleting field 'Page.name'
        db.delete_column(u'main_page', 'name')

        # Deleting field 'Page.slug'
        db.delete_column(u'main_page', 'slug')

        # Deleting field 'Page.section'
        db.delete_column(u'main_page', 'section_id')

        # Adding field 'File.subsection'
        db.add_column(u'main_file', 'subsection',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['main.SubSection']),
                      keep_default=False)

        # Deleting field 'File.page'
        db.delete_column(u'main_file', 'page_id')


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
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Section']"}),
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