from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from otipl import settings

sn = settings.SCRIPT_NAME[1:] + '/'
import tinymce 
urlpatterns = patterns('',
    # Examples:
    # url(r'^otipl/', include('otipl.foo.urls')),
    # url(r'^otipl/(?P<slug>.*)$', 'main.views.otipl', name='otipl'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^%s' % sn, include('attachment.urls')),
    url(r'^%sadmin/doc/' % sn, include('django.contrib.admindocs.urls')),
    url(r'^%stinymce/' %sn, include('tinymce.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^%sadmin/' % sn, include(admin.site.urls)),
    url(r'^%sstaff/(?P<name>.*)$' % sn, 'main.views.staff', name='staff'),   
    url(r'^%sfiles/(?P<path>.*)$' % sn, 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^%sprofile/edit$' % sn, 'main.views.edit', name='edit'),
    url(r'^%scheck_user$' % sn, 'main.views.check_user', name='check_user'),
    url(r'^%sis_email_avail$' % sn, 'main.views.is_email_avail', name='is_email_avail'),
    url(r'^%slogin$' % sn, 'main.views.login_user', name='login'),  
    url(r'^%slogout$' % sn, 'main.views.logout_user', name='logout'),        
    url(r'^%ssave$' % sn, 'main.views.save', name='save'),            
    url(r'^%s(?P<slug>.*)$' % sn, 'main.views.otipl', name='otipl'),
)
