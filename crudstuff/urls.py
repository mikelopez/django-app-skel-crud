from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # /root-url/service-name/action/object_id
    # /customers/customers/show/24
    # ordering of urls matters here...
    url(r'(?P<model>\w+)/(?P<action>\w+)/(?P<id>\w+)$','crudstuff.views.index'),
    url(r'(?P<model>\w+)/(?P<action>\w+)$','crudstuff.views.index'),
    url(r'(?P<model>\w+)$','crudstuff.views.index' ),
    url(r'^$', 'crudstuff.views.index', name='crudstuff_index'),
    

    #url(r'^(?P<customer_id>\w+)/(?P<object_id>\w+)','digiportal_customers.views.main_index', name="main_index_view")

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
