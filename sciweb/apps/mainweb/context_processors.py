from django.template import Context
import logging
log = logging.getLogger('mainweb.context_processors')

def index_data(request, linkname=None, filtername=None):
    """
    creating for possible future use
    """
    return {}

def admin_data(request):
    """
    creating for possible admin crud use
    """
    if not request.user.is_staff:
        return {}