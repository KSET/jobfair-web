from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'admin/login.html'}),
)
