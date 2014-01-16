from django.conf.urls import patterns, url

from calculate import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
