from pyshopzilla import *
from mainweb.tests.basetests import *

class TestShopzilla(BaseTestCase):
    """
    Test pyshopzilla 
    """

    def test_products(self):
        """
        Very Basic test: Tests our log class
        """
        data = {'apiKey': token, 'publisherId': pubtoken, 'keyword': '',\
        'resultsOffers': 50, 'productId': 'ps3', 'results': '250'}
    
        # to do - sanitize sarch_string 
        shop = ShopzillaAPI(**data)
        shop.bidded_only()
        shop.contains_images()
        shop.read_response(debug=True, debug_filename=debug_filename)
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
            offer_counter = 0
            for offer in i['offers']['offer']:
                try:
                    affiliated_products['products']['product'][counter]['offers']['offer'][offer_counter]['short_name'] = str(i['title'][:130])
                except KeyError:
                    pass
                offer_counter += 1
            counter += 1
        return affiliated_products
 
        #{'taxonomy': {'categories': {'category': [{'id': 1, 'name': 'Home', 'children': {'category': [{'

    def test_taxonomy(self):
        """
        Very Basic test: Tests our log class
        """
        data = {'apiKey': token, 'publisherId': pubtoken, 'keyword': '',\
        'results': '50', 'categoryId': '1'}
    
        # to do - sanitize sarch_string 
        shop = ShopzillaTaxonomyAPI(**data)
        
        shop.read_response(debug=True, debug_filename=debug_filename)
        try: 
            shop.parse_json()
        except:
            shop.json_data = shop.response_data

        categories = shop.json_data
        cats = categories.get('taxonomy').get('categories').get('category')[0].get('children').get('category')
        #print cats
        for i in cats:
            try:
                s = ShopCategory.objects.get(shop_id=i.get('id'))
                print '%s|%s' % (s.name, s.shop_id)
            except ShopCategory.DoesNotExist:
                s = ShopCategory(shop_id=i.get('id'), name=i.get('name'))
                s.save()
                print '%s|%s' % (s.name, s.shop_id)


