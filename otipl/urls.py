from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from otipl import settings

sn = settings.SCRIPT_NAME[1:] + '/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^otipl/', include('otipl.foo.urls')),
    # url(r'^otipl/(?P<slug>.*)$', 'main.views.otipl', name='otipl'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^%sadmin/doc/' % sn, include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^%sadmin/' % sn, include(admin.site.urls)),
    url(r'^%sfiles/(?P<path>.*)$' % sn, 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^%s(?P<slug>.*)$' % sn, 'main.views.otipl', name='otipl'),
)
