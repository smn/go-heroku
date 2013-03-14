from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from goapp import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'goapp.views.home', name='home'),
    # url(r'^goapp/', include('goapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^messages\.json$', views.messages),
)
