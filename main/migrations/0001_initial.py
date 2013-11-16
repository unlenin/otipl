# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TestModel'
        db.create_table(u'main_testmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'main', ['TestModel'])

        # Adding model 'Section'
        db.create_table(u'main_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'main', ['Section'])

        # Adding M2M table for field subsections on 'Section'
        m2m_table_name = db.shorten_name(u'main_section_subsections')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('section', models.ForeignKey(orm[u'main.section'], null=False)),
            ('subsection', models.ForeignKey(orm[u'main.subsection'], null=False))
        ))
        db.create_unique(m2m_table_name, ['section_id', 'subsection_id'])

        # Adding model 'SubSection'
        db.create_table(u'main_subsection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'main', ['SubSection'])

        # Adding model 'Page'
        db.create_table(u'main_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=30000)),
            ('subsection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.SubSection'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Section'])),
        ))
        db.send_create_signal(u'main', ['Page'])


    def backwards(self, orm):
        # Deleting model 'TestModel'
        db.delete_table(u'main_testmodel')

        # Deleting model 'Section'
        db.delete_table(u'main_section')

        # Removing M2M table for field subsections on 'Section'
        db.delete_table(db.shorten_name(u'main_section_subsections'))

        # Deleting model 'SubSection'
        db.delete_table(u'main_subsection')

        # Deleting model 'Page'
        db.delete_table(u'main_page')


    models = {
        u'main.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '30000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Section']"}),
            'subsection': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.SubSection']"})
        },
        u'main.section': {
            'Meta': {'ordering': "['order']", 'object_name': 'Section'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'subsections': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.SubSection']", 'symmetrical': 'False'})
        },
        u'main.subsection': {
            'Meta': {'ordering': "['order']", 'object_name': 'SubSection'},
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