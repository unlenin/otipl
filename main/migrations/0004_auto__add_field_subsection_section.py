# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field subsections on 'Section'
        db.delete_table(db.shorten_name(u'main_section_subsections'))

        # Adding field 'SubSection.section'
        db.add_column(u'main_subsection', 'section',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['main.Section']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding M2M table for field subsections on 'Section'
        m2m_table_name = db.shorten_name(u'main_section_subsections')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('section', models.ForeignKey(orm[u'main.section'], null=False)),
            ('subsection', models.ForeignKey(orm[u'main.subsection'], null=False))
        ))
        db.create_unique(m2m_table_name, ['section_id', 'subsection_id'])

        # Deleting field 'SubSection.section'
        db.delete_column(u'main_subsection', 'section_id')


    models = {
        u'main.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '30000'}),
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