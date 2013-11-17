from django.db import models

from orderedmodel import OrderedModel

from django.db import models
from django.core.files.storage import FileSystemStorage

from otipl.settings import PROJECT_DIR

import os

from django.db import models
from tinymce import models as tinymce_model

fs = FileSystemStorage(location=os.path.join(PROJECT_DIR, "files"))

class File(models.Model):
    page = models.ForeignKey('Page')
    file = models.FileField(upload_to="file-%Y%m%d-%H%M", storage=fs)

    def __unicode__(self):
        return unicode(self.file) + " in " + unicode(self.page)

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
    created_at = models.DateTimeField(auto_now_add = True)
    show = models.BooleanField()

    def __unicode__(self):
    	return self.header
# Create your models here.
