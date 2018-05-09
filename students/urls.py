from django.conf.urls import url
from . import views
app_name = 'students'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new_student, name='new_student'),
    url(r'^new/attendance/$', views.new_attendance, name='new_attendance'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/detail/attendance/$', views.attendance, name='attendance'),
]
from django.conf.urls import url
from . import views
app_name = 'students'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new_student, name='new_student'),
    url(r'^new/attendance/$', views.new_attendance, name='new_attendance'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/detail/attendance/$', views.attendance, name='attendance'),
]
