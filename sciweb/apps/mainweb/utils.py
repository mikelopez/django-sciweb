from pyshopzilla import *
# used for mainweb.views controller for common functions

def get_meta_domain(request, logger=False):
    """ 
    Return website object by http data - no mistakes 
    use this to get the domain name to search for a specific sitepage
    and website
    """
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

def shopzilla_search(pubtoken, token, search_for, debug=False, debug_filename=None):
    """
    Perform API search 
    requires: pubtoken, token, search_for (string)
    optional debug to create a file output
    and debug_filename specifies which debug file to write
    """ 
    data = {'apiKey': token, 'publisherId': pubtoken, 'keyword': search_for,\
        'resultsOffers': 3, 'productId': ''}

    # to do - sanitize sarch_string 
    shop = ShopzillaAPI(**data)
    shop.read_response(debug=debug, debug_filename=debug_filename)
    try: 
        shop.parse_json()
    except:
        shop.json_data = shop.response_data

    affiliated_products = shop.json_data
    try: 
        if not affiliated_products.get('products', None):
            affiliated_products = {'products': {'product':[]} }
    except AttributeError:
        affiliated_products = {'products': {'product':[]} }

    counter = 0  
    for i in affiliated_products['products']['product']:
        try: 
            rel = long(i['relevancy'])
            affiliated_products['products']['product'][counter]['relevancy'] = rel  
            affiliated_products['products']['product'][counter]['relevancy_string'] = str(rel)
        except KeyError:
            pass 
        counter += 1
    return affiliated_products