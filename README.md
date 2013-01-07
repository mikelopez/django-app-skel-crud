<h3>Project README for django-app-skel-crud</h3><br />
<hr />
http://django-app-skel-crud.readthedocs.org <br />
dev@scidentify.info - Marcos Lopez
<hr />
<br />
This is a very basic outline of a reusable django project/application. It will read its url entries that are defined, and by requesting a specific URL string (http://www.site.com/main/service/model-name/show/23) you will be able to do show/add/edit/delete functions through a single view controller to avoid code repetition.<br />

From inside this application, you can then include other smaller reusable apps and include the model definitions here. (See "other_reusable_app" folder for more info on this)

Basic Django knowledge is required, and some small bit of tuning is required in the files since they are vaguely named for demo purpose. 
<br />

<b>Installation</b><br />- add "django.template.loaders.eggs.Loader" to your TEMPLATE_LOADERS in settings.py<br />
- add app-name to INSTALLED_APPS in settings.py<br />
- (optional) add url(r'^app_name/', include('app_name.urls')), to your urls.py file (project)<br />
<h4>Installing instructions</h4><br />
(Todo: script these steps into deployment...)
To set this application up the right way, you will need to do some things to your project configuration, and your app_folder configuration. You can use the demo_project or use your own if you have already started a main project<br />
- Pick a desired app-name<br />
<b>Application implementation</b>
- update setup.py - replace "app_folder_name" with your desired app name
- change folder app_folder_name to the application name you would like
- replace "app_folder_name" in MANIFEST.in file with your app name
- modify conf.py as needed in your docs/ directory
- modify urls.py inside the app_folder, and replace app_folder_name with your app-name
- modify views.py file and change logger instance name
- modify views.py and change the class-table names and forms inside of data dictionary
- modify tests.py to change your models around to the actual table classes<br />
<b>Project configuration </b><br />
- modify your PROJECTS (see demo_project folder) urls.py file to include this apps urls.py file 
with a root-url (See: reusable-main in demo_project/urls). E.g http://www.site.com/root-url-name/services/model-name/action/ID
- modify your projects settings.py file, replace "demo_project" with your project name in ROOT_URLCONF, and WSGI_APPLICATION variables, and update any other settings you would like here.
- modify wsgi.py and replace demo_project with your project name


