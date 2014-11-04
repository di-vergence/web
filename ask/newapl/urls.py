from django.conf.urls import patterns, url

from newapl import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
   # url(r'^$', views.get, name='get')
)