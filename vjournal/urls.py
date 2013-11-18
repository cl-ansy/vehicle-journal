from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'vjournal.apps.vjournal.views.index', name='index'),

    #user account urls
    url(r'^account/login/$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'account/logout.html'}),
    url(r'^account/register/$', 'vjournal.apps.vjournal.views.register', name='regsiter'),

    #urls to add entries to database
    #these should probably be combined later into 1 page for a better UX
    url(r'^add/vehicle/$', 'vjournal.apps.vjournal.views.add_vehicle', name='add_vehicle'),
    url(r'^add/history/$', 'vjournal.apps.vjournal.views.add_history', name='add_history'),
    url(r'^add/mechanic/$', 'vjournal.apps.vjournal.views.add_mechanic', name='add_mechanic'),
    url(r'^add/finance/$', 'vjournal.apps.vjournal.views.add_finance', name='add_finance'),
    url(r'^add/part/$', 'vjournal.apps.vjournal.views.add_part', name='add_part'),

    #url for each history to AJAXically ( :^) ) show on index page

    #admin urls
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
