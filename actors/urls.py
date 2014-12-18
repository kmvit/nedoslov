from django.conf.urls import patterns, url
from django.contrib import admin
from actors import views


urlpatterns = patterns('',
    url(r'^$', views.actors, name='actors'),
    url(r'^(?P<slug>[\w\-]+)/$', views.actor_view,name="actor_view"),
)
