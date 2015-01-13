from django.conf.urls import *
#patterns, url
from newapl import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index')
    url(r'login', views.login, name="login"),
    url(r'signup', views.signup, name="signup"),
    url(r'question/(?P<question_id>\d)', views.question, name='question'),
    # url(r'register',views.register,name="register")
    url(r'^', views.index),
   # url(r'^$', views.get, name='get')
)