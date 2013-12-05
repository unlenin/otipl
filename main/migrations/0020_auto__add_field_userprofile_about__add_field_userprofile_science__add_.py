# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserProfile.about'
        db.add_column(u'main_userprofile', 'about',
                      self.gf('django.db.models.fields.CharField')(max_length=30000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.science'
        db.add_column(u'main_userprofile', 'science',
                      self.gf('django.db.models.fields.CharField')(max_length=30000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.teaching'
        db.add_column(u'main_userprofile', 'teaching',
                      self.gf('django.db.models.fields.CharField')(max_length=30000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.publications'
        db.add_column(u'main_userprofile', 'publications',
                      self.gf('django.db.models.fields.CharField')(max_length=30000, null=True, blank=True),
                      keep_default=False)


        # Changing field 'UserProfile.status'
        db.alter_column(u'main_userprofile', 'status', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'UserProfile.middle_name'
        db.alter_column(u'main_userprofile', 'middle_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'UserProfile.education'
        db.alter_column(u'main_userprofile', 'education', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):
        # Deleting field 'UserProfile.about'
        db.delete_column(u'main_userprofile', 'about')

        # Deleting field 'UserProfile.science'
        db.delete_column(u'main_userprofile', 'science')

        # Deleting field 'UserProfile.teaching'
        db.delete_column(u'main_userprofile', 'teaching')

        # Deleting field 'UserProfile.publications'
        db.delete_column(u'main_userprofile', 'publications')


        # Changing field 'UserProfile.status'
        db.alter_column(u'main_userprofile', 'status', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'UserProfile.middle_name'
        db.alter_column(u'main_userprofile', 'middle_name', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'UserProfile.education'
        db.alter_column(u'main_userprofile', 'education', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        },
        u'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about': ('django.db.models.fields.CharField', [], {'max_length': '30000', 'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'publications': ('django.db.models.fields.CharField', [], {'max_length': '30000', 'null': 'True', 'blank': 'True'}),
            'science': ('django.db.models.fields.CharField', [], {'max_length': '30000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'teaching': ('django.db.models.fields.CharField', [], {'max_length': '30000', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_profile'", 'to': u"orm['auth.User']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['main']