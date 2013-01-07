from django import forms
from models import School, Student

import logging
log = logging.getLogger('app_folder_name.views')

class SchoolForm(forms.ModelForm)
    """
    Customer form for input/edit
    """
    class Meta:
        # exclude any fields from the db here
        # exclude = ('accounts', 'status')
        model = School

    def clean(self):
        return self.cleaned_data

    def save(self, obj=None):
        """
        Edit the school object if id==True
        obj is a model() object or get result
        """
        if obj:
            school = obj
            for k, v in self.cleaned_data.items():
                setattr(school, k, v)
            school.save()



class StudentsForm(forms.ModelForm):
    """
    Students form
    """
    class Meta:
        model = Students


