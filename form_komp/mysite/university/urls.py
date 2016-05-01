from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.university_list, name='university_list'),
    url(r'^(?P<slug>[-\w]+)/$', views.trprog_list, name='trprog_list'),
]