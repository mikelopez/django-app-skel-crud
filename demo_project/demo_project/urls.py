from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login,logout
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from settings import PROJECT_ROOTDIR
urlpatterns = patterns('',
    # Examples:    
    url(r'^reusable-main/', include('app_folder_name.urls')),
    
    
    url(r'^login/', login),
    url(r'^logout/', logout, {'template_name': 'registration/login.html'}),
    url(r'^accounts/login', login),
    url(r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (PROJECT_ROOTDIR), 'show_indexes': True}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
