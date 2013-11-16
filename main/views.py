from django.http import HttpResponse
from django.shortcuts import render

from models import Section, Page, NewsItem, File

from django.core.files import File as DjFile
import os
from otipl.settings import PROJECT_DIR, SCRIPT_NAME

def make_news():
    news = NewsItem.objects.filter(show=True).order_by('-created_at')
    return ('<br>'+'.'*50).join(["<h5>%s %s</h5> %s" % (n.created_at.strftime("%d-%m-%Y"), n.header, n.content) for n in news])

def index(request, slug=''):
    sections = Section.objects.all()
    # slug = '/' + slug
    pages = Page.objects.filter(slug=slug)
    page = ''
    files = []
    if pages:
    	page = pages[0]
        files = page.file_set.all()
    dj_files = []
    for f in files:
        dj_files += [f.file]
    free_sec = Page.objects.filter(section__isnull=True)
    context = {'sections': sections, 'page': page, 'slug': slug, 'news': make_news(), 'files': dj_files, 'free_sec': free_sec}

    return render(request, 'main/index.html', context)

def otipl(request, slug=''):
    sections = Section.objects.all()
    # slug = '/' + slug
    pages = Page.objects.filter(slug=slug)
    page = ''
    files = []
    if pages:
        page = pages[0]
        files = page.file_set.all()
    dj_files = []
    for f in files:
        dj_files += [f.file]
    free_sec = Page.objects.filter(section__isnull=True,on_left_bar=False,get_pass_button=False)
    left_bar = Page.objects.filter(on_left_bar=True)
    get_pass = Page.objects.filter(get_pass_button=True)
    context = {'sections': sections, 
                'page': page, 
                'slug': slug, 
                'news': make_news(), 
                'files': dj_files, 
                'free_sec': free_sec, 
                'left_bar': left_bar,
                'get_pass_button': get_pass[0] if get_pass else ''}
    request.META['SCRIPT_NAME'] = SCRIPT_NAME
    return render(request, 'main/otipl.html', context)


