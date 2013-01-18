# used for mainweb.views controller for common functions

def get_meta_domain(request, logger=False):
    """ return website object by http data - no mistakes 
    use this to get the domain name to search for a specific sitepage
    and website"""
    try:
        sitename = request.get('HTTP_HOST')
    except AttributeError:
        sitename = None
    # if request.get returned None
    if not sitename:
        sitename = request.META.get('HTTP_HOST')
    domain_string = sitename.split(':')[0]
    if not domain_string:
        return None
    if logger:
        try:
            logger.info("utils.get_meta_domain: domain %s" % (domain_string))
        except:
            pass
    return domain_string.replace('http://', '').replace('www.','')