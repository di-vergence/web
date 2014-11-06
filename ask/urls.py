from django.conf.urls import patterns, include, url
from django.contrib import admin
#from grub import Grab
#from ask import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^newapl/', include('newapl.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('newapl.urls')),
   # url(r'^$', views.index, name='index'))
)
