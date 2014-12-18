from django.conf.urls import patterns, url
from django.contrib import admin
from afisha import views


urlpatterns = patterns('',
    url(r'^$', views.afisha_view, name='afisha_view'),
)
