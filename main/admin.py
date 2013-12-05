from django.contrib import admin
from orderedmodel import OrderedModelAdmin

from models import TestModel, Section, Page,NewsItem,File,UserProfile

from django import forms

class PageModelForm( forms.ModelForm ):
    #content = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Page

class PageAdmin(OrderedModelAdmin):
    #form = PageModelForm
    exclude = ('order', )
    list_display = ['name', 'section', 'reorder']

class TestModelAdmin(OrderedModelAdmin):
    list_display = ['name', 'reorder']

# class SubSectionInline(admin.StackedInline):                                                                                               
#     model = Section.subsections.through

class SectionAdmin(OrderedModelAdmin):
#     #filter_horizontal = ('subsections',)
#     inlines = [SubSectionInline,]
    exclude = ('order', )
    list_display = ['name', 'reorder']



admin.site.register(TestModel, TestModelAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(NewsItem)
admin.site.register(File)
admin.site.register(UserProfile)