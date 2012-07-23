from django.conf.urls import patterns, include, url
from staticweb.views import index_home
from userProfile.views import login, logout, signup
from courses.views import courses_all

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # static pages
    url(r'^$', index_home),

    # registration and login/logout related pages
    url(r'^accounts/signup/$', signup),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),

    # courses
    url(r'^courses/all/$', courses_all),
    url(r'^courses/home/$', index_home)
)
