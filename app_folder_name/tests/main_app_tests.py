"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import logging
from app_folder_name.models import School, Students 
from app_folder_name.forms import SchoolForm, StudentsForm

class TestSchoolStudents(TestCase):
    """
        Test the app_folder_name application
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_school_students(self):
        """ test adding a school to the database """
        school_attr = {'name': 'SchoolABC', 'district': 'District-XYZ', 'address': '200 SE 1 st City, STATE 33131' }

        school = School()
        for k, v in attrs.items():
            self.assertTrue(hasattr(school, 'name'))
            setattr(school, k, v)
        school.save()
        school.delete()
        self.assertTrue(len(School.objects.filter(name='SchoolABC') == 0))

        # save the customer with FORM
        school = SchoolForm(school_attrs)
        school.save(obj_to_update=School())

        # make sure the customer was created
        self.assertTrue(len(School.objects.filter(name='SchoolABC') == 1))
        school_get = School.objects.filter(name='SchoolABC')[0]

        # test EDIT the customer with form
        school_attrs_copy = customer_attrs
        school_attrs_copy['name'] = 'SchoolABC123'
        school_edit = SchoolForm(school_attrs_copy)
        school_edit.save(obj_to_update=school_get)

        # make sure entry was uupdated
        self.assertTrue(len(School.objects.filter(name='SchoolABC123')) == 1)
        school_update_get = School.objects.filter(name='SchoolABC123')[0]

        # make sure it wasnt really duplicated - but edited!
        self.assertTrue(len(School.objects.filter(name='SchoolABC')) == 0)




    def test_settings(self):
        """ check settings for vars we need """
        try:
            from settings import PROJECT_ROOTDIR
        except:
            print 'PROJECT_ROOTDIR not found in settings'
            raise AssertionError

        try:
            from settings import STATIC_BOOTSTRAP
        except:
            print 'STATIC_BOOTSTRAP not found in settings'
            raise AssertionError


    def test_urlstructures(self):
        """
        test the URL structures to make sure we can obtain the 
        right model and form objects needed for updating/viewing

        MODIFY THIS if you are changing the models around
        """
        urlstring = '/reusable-main/school-records/schools/show/1'
        from app_folder_name.views import process_url
        model, form = process_url(urlstring)

        self.assertTrue(isinstance(model, School))
        self.assertTrue(isinstance(form, SchoolForm))

        response = c.get(urlstring)
        # make sure the url is found, its ok if we get redirection or 500
        self.assertTrue(response.status_code != '404')
        


