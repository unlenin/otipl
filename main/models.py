from django.db import models

from orderedmodel import OrderedModel

from django.db import models
from django.core.files.storage import FileSystemStorage

from otipl.settings import PROJECT_DIR

import os

from django.db import models
from tinymce import models as tinymce_model
from django.contrib.auth.models import User

fs = FileSystemStorage(location=os.path.join(PROJECT_DIR, "files"))

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^tinymce\.models.\HTMLField"])

class File(models.Model):
    page = models.ForeignKey('Page')
    file = models.FileField(upload_to="file-%Y%m%d-%H%M", storage=fs)

    def __unicode__(self):
        return unicode(self.file) + " in " + unicode(self.page)

class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name="user_profile")
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    grade = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='pic_folder/')
    about = models.CharField(max_length=30000, blank=True, null=True)
    science = models.CharField(max_length=30000, blank=True, null=True)
    teaching = models.CharField(max_length=30000, blank=True, null=True)
    publications = models.CharField(max_length=30000, blank=True, null=True)
    def __unicode__(self):
        return self.user.username

class TestModel(OrderedModel):
    name = models.CharField(max_length=30)



class Section(OrderedModel):
    name = models.CharField(max_length=30)
# 	Name
    def __unicode__(self):
        return self.name

class Page(OrderedModel):
    content = tinymce_model.HTMLField() #models.CharField(max_length=30000)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True)
    section = models.ForeignKey(Section, blank=True, null=True)
    on_left_bar = models.BooleanField()
    get_pass_button = models.BooleanField()    
    #section = models.ForeignKey(Section)

    def __unicode__(self):
    	return (self.section.name if self.section else '') + '/' + self.name

class NewsItem(models.Model):
    header = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    scheduled = models.DateTimeField()
    valid_until = models.DateTimeField()    
    created_at = models.DateTimeField(auto_now_add = True)
    show = models.BooleanField()

    def __unicode__(self):
    	return self.header
# Create your models here.
