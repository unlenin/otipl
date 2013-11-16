from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from otipl import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^otipl/', include('otipl.foo.urls')),
    # url(r'^otipl/(?P<slug>.*)$', 'main.views.otipl', name='otipl'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^(?P<slug>.*)$', 'main.views.otipl', name='otipl'),
)
