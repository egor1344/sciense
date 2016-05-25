from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.course_list, name='course_list'),
    url(r'^(?P<slug>[-\w]+)/xlsx/$',
        views.trainprog_xlsx,
        name='trainprog_xlsx'),
    url(r'^(?P<slug>[-\w]+)/(?P<slug_c>[-\w]+)/$',
        views.course_detail,
        name='course_detail'),
    url(r'^(?P<slug>[-\w]+)/(?P<slug_c>[-\w]+)/xlsx/$',
        views.course_xlsx,
        name='course_xlsx'),
]
