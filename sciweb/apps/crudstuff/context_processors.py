from django.template import Context
from django.contrib.contenttypes.models import ContentType
import logging
log = logging.getLogger('crudstuff.context_processors')
from bindmodels import admin_models

def admin_data(request):
    """
    get the model name and return model instance
    possible actions are: add, edit, show
    id optional with action show
    id required with action edit
    return data dictionary
    """
    if not request.user.is_staff:
        log.info('Not admin')
        return {}

    model_name = request.session.get('model')
    action = request.session.get('action')
    value = request.session.get('id')

    model = None
    models_list = None
    model_values = None

    # get the model
    if model_name:
        log.info('Model set to %s' % model_name)
        try:
            ctype = ContentType.objects.get(model=model_name)
        except ContentType.DoesNotExist:
            log.info('Model does not exist %s' % model_name)
            raise Exception('Model does not exist')
        model = ctype.model_class()

    # return the models list for nav
    log.info('returing model list')
    models_list = admin_models

    if model:
        if action == 'show':
            model_values = model.objects.all()
        if action == 'edit':
            pass
        if action == 'add':
            pass
        if action == 'remove':
            pass

    
    return {'model_name': model_name, 'model': model, 'action': action, 'value': value,\
        'models_list': models_list, 'model_values': model_values}
    