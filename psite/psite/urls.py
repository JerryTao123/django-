from django.conf.urls import patterns, include, url
from django.contrib import admin

from page import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'psite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^$', views.index, name= 'home'),
   url(r'^lin/', views.lin, name= 'lin'),
   url(r'^about/', views.about, name= 'about'),
    url(r'^admin/', include(admin.site.urls)),
   # url(r'^blog/', include('blog.urls')),
)
