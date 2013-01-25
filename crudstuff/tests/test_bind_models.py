"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import logging
import os, sys
import importlib

from django.conf import settings

#sys.path.append(os.path.dirname(os.path.realpath(__file__)))
#print os.path.realpath(os.path.dirname(__file__))
#sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from django.test import TestCase


class TestBindModels(TestCase):
    """
    Make sure the settings file contains the data needed
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_the_settings_override(self):
        """
        Test the settings override and make sure that they are overriden!
        """
        from crudstuff.bindmodels import admin_models
        data = admin_models(settings=settings)

        # make sure the test model string is in settings so we can check for it
        self.assertTrue(getattr(settings, 'TEST_MODEL_NAME', 'website'))

        # make sure the test_model_name exists in the admin data dict 
        # which shoudl auto append it
        self.assertTrue(data.models.get(getattr(settings, 'TEST_MODEL_NAME', 'website')))
        self.assertTrue(data.forms.get(getattr(settings, 'TEST_MODEL_NAME', 'website')))


    def test_defaults(self):
        """
        Test to make sure the values inside of the bindmodels class are 
        tied to the right forms
        """
        from crudstuff.bindmodels import admin_models
        data = admin_models(settings=settings)
        for k, v in data.models.items():
            # check for the form created for the model
            if not data.forms.get(k):
                assert False

            print 'Found form for apps.%s.forms.%s' % (data.models.get(k), data.forms.get(k))
            mainweb_forms = importlib.import_module('%s.forms' % (data.models.get(k)))
            # test init the model
            form = getattr(mainweb_forms, data.forms.get(k))
            self.assertTrue(form)
            form_instance = form()
            self.assertTrue(form_instance)





