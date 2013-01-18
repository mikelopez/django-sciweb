from django.template import Context
from django.contrib.contenttypes.models import ContentType
import logging
log = logging.getLogger('crudstuff.context_processors')


def admin_data(request):
    """
    get the model name and return model instance
    possible actions are: add, edit, show
    id optional with action show
    id required with action edit
    return data dictionary
    """
    if not request.user.is_staff:
        return {}
    model_name = request.session.get('model')
    action = request.session.get('action')
    value = request.session.get('id')

    # get the model
    try:
        ctype = ContentType.objects.get(model=model_name)
    except ContentType.DoesNotExist:
        log.info('Model does not exist %s' % model_name)
        raise Exception('Model does not exist')

    model = ctype.model_class()
    return {'model': model, 'action': action, 'value': value}
    