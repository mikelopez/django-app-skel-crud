__author__ = 'Marcos Lopez'
__email__ = 'dev@scidentify.info' 

from django.db import models
from django.contrib.auth.models import User
from django import forms

# UPDATE your models here.

from countrycodes import COUNTRY_STATES
from django.conf import settings

PROJECT_ROOTDIR = settings.PROJECT_ROOTDIR

class School(models.Model):
  """
  very basic school model 
  """
  name = models.CharField(max_length=40)
  address = models.CharField(max_length=40)
  district = models.CharField(max_length=40)

class Student(models.Model):
  """
  very basic student model - assigned to a school 
  """
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  school = models.ForeignKey('School')

