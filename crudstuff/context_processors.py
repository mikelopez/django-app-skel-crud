from django.template import Context
from django.contrib.contenttypes.models import ContentType
import logging
log = logging.getLogger('crudstuff.context_processors')
from bindmodels import admin_models
from django.conf import settings

# Set the logging
DEBUG_CRUD = getattr(settings, "DEBUG_CRUD", False)
if DEBUG_CRUD:
  hdlr = logging.StreamHandler()
  formatter = logging.Formatter('\n--\nLOG :: %(asctime)s %(levelname)s %(message)s \n---')
  hdlr.setFormatter(formatter)
  log.addHandler(hdlr)
  log.setLevel(logging.INFO)
  log.setLevel(logging.DEBUG)


def admin_data(request):
    """
    get the model name and return model instance
    possible actions are: add, edit, show
    id optional with action show
    id required with action edit
    return data dictionary
    """

    model_name = request.session.get('model')
    action = request.session.get('action')
    value = request.session.get('id')

    model = None
    models_list = None
    model_values = None
    model_form = None
    posted = True if request.method == 'POST' else False

    log.info("action %s" % action)

    # set the model
    if model_name:
        log.info('Model set to %s' % model_name)
        try:
            ctype = ContentType.objects.get(model=model_name)
        except ContentType.DoesNotExist:
            log.info('Model does not exist %s' % model_name)
            raise Exception('Model does not exist')
        model = ctype.model_class()

    # return the models list for nav
    admin_class = admin_models(settings=settings)
    models_list = admin_class.models.keys()

    # if model is set, check show/add/remove actions
    if model:
        model_form = admin_class.get_form_by_model(model_name)

        if action == 'show':
            model_values = model.objects.all()

        if action == 'edit':
            if not value:
                log.info('Edit value not set...')
            if value:
                if request.method == 'POST':
                    log.info('Processing EDIT POST')
                    model_form = model_form()
            
        if action == 'add':
            if request.method == 'POST':
                log.info('Processing POST')
                model_form = model_form(request.POST)
                if model_form.is_valid():
                    log.info('Form is valid...saving it')
                    model_form.save()
            
        if action == 'remove':
            pass

    
    return_dict = {'model_name': model_name, 'model': model, 'action': action, 'value': value,\
        'models_list': models_list, 'model_values': model_values, 'model_form': model_form, \
        'posted': posted}
    return Context(return_dict)
    
