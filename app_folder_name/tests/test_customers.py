"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import logging

class TestSchoolStudents(TestCase):
    """
        Test the app_folder_name application
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_customer(self):
        """ test adding a customer to the database """
        customer_attrs = {'name': 'Customer Test', 'status': 'active', 'address': '200 se 1 st', \
            'city': 'miami', 'state': 'FL'}

        customer = Customer()
        for k, v in attrs.items():
            self.assertTrue(hasattr(customer, 'name'))
            setattr(customer, k, v)
        customer.save()
        customer.delete()
        self.assertTrue(len(Customer.objects.filter(name='Customer Test') == 0))

        # save the customer
        customer = CustomerForm(customer_attrs)
        customer.save(obj_to_update=Customer())

        # make sure the customer was created
        self.assertTrue(len(Customer.objects.filter(name='Customer Test') == 1))
        customer_get = Customer.objects.filter(name='Customer Test')[0]

        # test updating the customer
        customer_attrs_copy = customer_attrs
        customer_attrs_copy['name'] = 'COMPANY123'
        customer_edit = CustomerForm(customer_attrs)
        customer_edit.save(obj_to_update=Customer.objects.get())

        # make sure entry was created
        self.assertTrue(len(Customer.objects.filter(name='COMPANY123')) == 1)
        customer_update_get = Customer.objects.filter(name='COMPANY123')[0]

        # make sure it wasnt really duplicated - but edited!
        self.assertTrue(len(Customer.objects.filter(name='Customer Test')) == 0)




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
        urlstring = '/customers/customers/customer/show/1'
        from digiportal_customers.views import process_url
        model, form = process_url(urlstring)

        self.assertTrue(isinstance(model, Customer))
        self.assertTrue(isinstance(form, CustomerForm))

        response = c.get(urlstring)
        # make sure the url is found, its ok if we get redirection or 500
        self.assertTrue(response.status_code != '404')
        


