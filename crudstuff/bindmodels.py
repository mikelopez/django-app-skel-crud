import importlib

class admin_models:
    """ 
    class wrapper for admin_models data dict 
    if using as a pluggable app via setup tools, make
    sure to override models and forms with 
    data from your projects settings. if you copied the 
    application folder local to your project then you can just 
    edit models and forms here and keep exclude the settings options
    """
    model_tables = {
        'website': 'Website',
        'websitepage': 'WebsitePage',
    }
    models = {
        'website': 'mainweb',
        'websitepage': 'mainweb'
    }
    forms = {
        'website': 'WebsiteForm', 
        'websitepage': 'WebsitePageForm'
    }

    def __init__(self, settings=None):
        """
        Check settings and override self.models and self.forms
        data dictionary if variables present in settings
        """
        if settings:
            try:
                if getattr(settings, 'CRUDSTUFF_MODELS'):
                    self.models = getattr(settings, 'CRUDSTUFF_MODELS')
            except AttributeError:
                pass
            try:
                if getattr(settings, 'CRUDSTUFF_FORMS'):
                    self.forms = getattr(settings, 'CRUDSTUFF_FORMS')
            except AttributeError:
                pass
            try:
                if getattr(settings, 'CRUDSTUFF_FORMS'):
                    self.model_tables = getattr(settings, 'CRUDSTUFF_MODEL_TABLES')
            except AttributeError:
              pass

    def get_app(self, k):
        """
        get the app name based on a model
        """
        return self.models.get(k)

    def get_app_by_model(self, k):
        """
        get the app name by the model name so that 
        we can know which app to look for forms in
        """
        if not k in self.models.keys():
            return None
        return self.models.get(k)


    def get_form_by_model(self, k):
        """
        get the form class instance by the model name and app name
        """
        app = self.get_app_by_model(k)
        if not app:
            raise Exception('App %s is not found for model %s ' % (app, k))

        forms_module = importlib.import_module('%s.forms'%(app))
        form = getattr(forms_module, self.forms.get(k))
        if not form:
            raise Exception('Form %s not found for %s ' % (data.forms.get(k), app))
        return form
