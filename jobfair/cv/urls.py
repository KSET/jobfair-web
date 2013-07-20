from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^new$', views.new, name='new'),
        url(r'^edit/$', views.edit_page, name='edit page'),
        url(r'^edit/(?P<access_code>\w+)/$', views.edit_profile, name='edit profile'),
        )
