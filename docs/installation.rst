.. _usage:

Installation
=====

- enable ``'django.template.loaders.eggs.Loader'`` in ``TEMPLATE_LOADERS`` in your ``settings.py`` file

To set this application up the right way, you will need to do some things to your project configuration, and your app_folder configuration. You can use the demo_project or use your own if you have already started a main project

Installing Application
======================
- Pick a desired app-name
- update ``setup.py`` - replace "app_folder_name" with your desired app name
- change ``folder app_folder_name`` to the application name you would like
- replace "app_folder_name" in ``MANIFEST.in`` file with your app name
- modify ``docs/conf.py`` as needed in your docs/ directory
- modify ``app_folder_name/urls.py``, and replace app_folder_name with your app-name
- modify ``app_folder_name/views.py`` file and change logger instance name. see sample below::
import logging
log = logging.getLogger('app_folder_name.views')

- modify ``views.py`` and change the class-table names and forms inside of data dictionary. See below::
"""
data structure
service_name: dictionary with key as model-name(url), and 
returns list of Model and Form instance 
E.g: get the model = data.get('customers').get('customer')[0]
E.g: get the form = data.get('customers').get('customer')[1]
"""
data = {
    #'other_apps': {
    #   'table-alias-name': [TableClass, TableClassForm],
    #   'other-table-alias': [TableClass, TableClassForm]
    #}
    'school_district': {
        'student': [Customer, CustomerForm],
        'school': [Contacts, ContactsForm],
    },
}

- modify ``tests/__init__.py``, replace ``app_folder_name`` with your app name and the proper filename to the tests you want to include
- modify ``tests/main_app_tests.py``, replace ``app_folder_name`` to your app-name, and change your models around to the actual table classes


Installing Project
========================
- modify your PROJECTS (see ``demo_project`` folder) urls.py file to include the app's ``urls.py`` file. See sample::
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
- modify ``demo_project/settings.py`` (or your custom projects), replace "demo_project" with your project name in ``ROOT_URLCONF`` and ``WSGI_APPLICATION`` variables, and update any other settings you would like here.
- modify ``demo_project/wsgi.py`` and replace demo_project with your project name (if using demo_project)
- add any other custom settings you might add to a project!


