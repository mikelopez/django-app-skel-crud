.. _usage:

Settings Configuring Installation
=================================

- enable ``'django.template.loaders.eggs.Loader'`` in ``TEMPLATE_LOADERS`` in your ``settings.py`` file

To set this application up the right way, you will need to do some things to your project configuration, and your app_folder configuration. You can use the demo_project or use your own if you have already started a main project

- add ``crudstuff.context_processprs.admin_data`` to TEMPLATE_CONTEXT_PROCESSORS on admin

- (optional) add ``DEBUG_CRUD = True`` to enable logging to stderr and stdout

Here is an example of my context processors entry on settings.py::

  TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "django.core.context_processors.static",
  "django.core.context_processors.tz",
  "django.contrib.messages.context_processors.messages",
  "crudstuff.context_processors.admin_data",)


Bind the models and forms
-------------------------
You will need to specify the models, the app name where that model class lives, and the form name associated with that model. 
The "name" field of the model is a lowercase string representation of the class name so that we can then perform a model_name search via the context_processors. See the code in context_processors.py 


modify ``settings.py`` and change the class-table names and forms inside of data dictionary. See below::

  CRUDSTUFF_MODELS = {
        'school': 'app_folder_name',
        'student': 'app_folder_name'
  }
  CRUDSTUFF_FORMS = {
          'school': 'SchoolForm', 
          'student': 'StudentsForm'
  }


Projects Configuration 
=====================
modify your PROJECTS (see ``demo_project`` folder) urls.py file to include the app's ``urls.py`` file. See sample::

  from django.conf.urls import patterns, include, url
  from django.contrib.auth.views import login,logout
  # Uncomment the next two lines to enable the admin:
  # from django.contrib import admin
  # admin.autodiscover()
  from settings import PROJECT_ROOTDIR
  urlpatterns = patterns('',
      # Examples:
      url(r'^crudstuff/', include('crudstuff.urls')),
      

      url(r'^login/', login),
      url(r'^logout/', logout, {'template_name': 'registration/login.html'}),
      url(r'^accounts/login', login),
      url(r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'%s/static/' % (PROJECT_ROOTDIR), 'show_indexes': True}),

      # Uncomment the admin/doc line below to enable admin documentation:
      # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

      # Uncomment the next line to enable the admin:
      #url(r'^admin/', include(admin.site.urls)),
  )


Some notes if you're copying from the project settings file

- modify ``demo_project/settings.py`` (or your custom projects), replace "demo_project" with your project name in ``ROOT_URLCONF`` and ``WSGI_APPLICATION`` variables, and update any other settings you would like here.
- modify ``demo_project/wsgi.py`` and replace demo_project with your project name (if using demo_project)
- add any other custom settings you might add to a project and enjoy!


