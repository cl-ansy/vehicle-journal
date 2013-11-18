from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'vjournal.apps.vjournal.views.index', name='index'),

    #user account urls
    url(r'^account/login/$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'account/logout.html'}),
    url(r'^account/register/$', 'vjournal.apps.vjournal.views.register', name='regsiter'),

    #admin urls
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
