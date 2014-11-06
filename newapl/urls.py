from django.conf.urls import *
#patterns, url
from newapl import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index')
    url(r'login', views.login, name="login"),
    url(r'signup', views.signup, name="signup"),
    url(r'^', views.index),
   # url(r'^$', views.get, name='get')
)