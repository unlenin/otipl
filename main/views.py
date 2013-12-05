from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render

from models import Section, Page, NewsItem, File, UserProfile

from django.core.files import File as DjFile
import os
from otipl.settings import PROJECT_DIR, SCRIPT_NAME

from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, AnonymousUser

import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import re

from forms import ImageUploadForm
@csrf_exempt
def check_user(request):
    email = request.POST['email']
    password = request.POST['password']
    users = User.objects.filter(email=email)
    r = {"valid": 0};
    if users:
        user = authenticate(username=users[0].username, password=password)

        if user and user.is_active:
            r["valid"] = 1;
    return HttpResponse(json.dumps(r));

@csrf_exempt
def is_email_avail(request):
    email = request.POST['email']
    r = {"busy": 0};
    if User.objects.filter(email=email).count() or not re.match("[^@]+@[^@]+\.[^@]+", email):
        r["busy"] = 1;
    return HttpResponse(json.dumps(r));

@csrf_exempt
def is_name_avail(request):
    name = request.POST['name']
    r = {"busy": 0};
    if User.objects.filter(username=name).count()  or not re.match("^[a-zA-Z0-9_.-]+$", name):
        r["busy"] = 1;
    return HttpResponse(json.dumps(r));

@csrf_exempt
def login_user(request):
    email = request.POST['email']
    password = request.POST['password']
    users = User.objects.filter(email=email)
    r = {"valid": 0};
    user = None
    if users:
        user = authenticate(username=users[0].username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("success")
        return HttpResponse("not_active")

    return HttpResponse("fail " + str(user))

@csrf_exempt
def logout_user(request):
    logout(request)
    return HttpResponse("success")
        
def make_news():
    news = NewsItem.objects.filter(show=True,valid_until__gte=date.today()).order_by('-created_at')
    return ('<br><hr align="center" width="80%" size="2" color="#ff0000" />').join(["<h5>%s %s</h5> %s" % (n.scheduled.strftime("%d-%m-%Y"), n.header, n.content) for n in news])

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

def free_email(request):
    data = {'html': request.POST['email']}
    return HttpResponse(json.dumps(data), mimetype="application/json")

def get_context(request):
    sections = Section.objects.all()    
    free_sec = Page.objects.filter(section__isnull=True,on_left_bar=False,get_pass_button=False)
    left_bar = Page.objects.filter(on_left_bar=True)
    get_pass = Page.objects.filter(get_pass_button=True)
    profile = ''
    if not isinstance(request.user, AnonymousUser):
        if not request.user.user_profile.all():
            profile = UserProfile()
            profile.user = request.user
            profile.save()

        profile = request.user.user_profile.all()[0]
    context = {'sections': sections, 
                'news': make_news(), 
                'free_sec': free_sec, 
                'left_bar': left_bar,
                'get_pass_button': get_pass[0] if get_pass else '',
                'profile': profile}
    return context

def edit(request):
    #create user profile
    status = ''
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            lastname = request.POST['lastname']
            firstname = request.POST['firstname']
            middlename = request.POST['middlename']
            status = request.POST.get('status','')
            education = request.POST.get('education','')
            year = request.POST.get('year','1')
            course = request.POST.get('course','1')
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            profile = UserProfile()
            profile.user = user
            profile.middle_name = middlename
            profile.status = status
            profile.education = education
            profile.grade = course
            profile.year = year
            profile.save()
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # get profile from user

            if not request.user.user_profile.all():
                profile = UserProfile()
                profile.user = request.user
                profile.save()

            m = request.user.user_profile.all()[0]
            status = m.status
            m.photo = form.cleaned_data['image']
            m.save()
        if 'about' in request.POST or 'teaching'  in request.POST or 'science' in request.POST or 'publications' in request.POST:
            if not request.user.user_profile.all():
                profile = UserProfile()
                profile.user = request.user
                profile.save()

            m = request.user.user_profile.all()[0]
            if 'about' in request.POST:
                m.about = request.POST.get('about','')
            if 'teaching' in request.POST:
                m.teaching = request.POST.get('teaching','')
            if 'science' in request.POST:
                m.science = request.POST.get('science','')
            if 'publications' in request.POST:
                m.publications = request.POST.get('publications','')
            m.save()

        context = get_context(request)
        context['type'] = status

        return render(request, 'main/edit.html', context)
    elif request.user.is_authenticated():
        context = get_context(request)
        if not request.user.user_profile.all():
            profile = UserProfile()
            profile.user = request.user
            profile.save()
        context['type'] = request.user.user_profile.all()[0].status

        return render(request, 'main/edit.html', context)       

    return HttpResponseForbidden('allowed only registered users or via POST')

def save(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # get profile from user
            if not request.user.user_profile.all():
                profile = UserProfile()
                profile.user = request.user
                profile.save()

            m = request.user.user_profile.all()[0]
            m.photo = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')

def staff(request, name):
    context = get_context(request)
    pages = Page.objects.filter(slug='staff/' + name)
    users = User.objects.filter(username=name)
    if pages or users:
        if pages:
            context["name"] = pages[0].name
            lastname,firstname,middlename = pages[0].name.split()
            users = User.objects.filter(first_name=firstname,last_name=lastname)
        else:
            user = users[0]
            context["name"] = "%s %s %s" % (user.last_name,user.first_name,user.user_profile.all()[0].middle_name)      

        
        if users:
            st_profile = users[0].user_profile.all()[0]
            context['st_profile'] = st_profile
    return render(request, 'main/staff.html', context) 

def otipl(request, slug=''):
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
    
    context = get_context(request)
    for k,v in {
                'page': page, 
                'slug': slug, 
                'news': make_news(), 
                'files': dj_files}.items():
        context[k] = v
    request.META['SCRIPT_NAME'] = SCRIPT_NAME
    return render(request, 'main/otipl.html', context)


