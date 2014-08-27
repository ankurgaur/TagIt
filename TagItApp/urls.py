from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from TagItApp.views import login, signup

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TagIt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^login/$', login),
    url(r'^signup/$', signup),
    url(r'^admin/', include(admin.site.urls)),
)
