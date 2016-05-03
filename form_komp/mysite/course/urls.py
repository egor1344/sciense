from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.course_list, name = 'course_list'),
    url(r'^(?P<slug>[-\w]+)/(?P<slug_c>[-\w]+)/$', views.course_detail, name='course_detail'),
]