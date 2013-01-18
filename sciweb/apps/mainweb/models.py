from django.db import models
from django.core.exceptions import ValidationError
from settings import STATIC_PAGES

blankfield = {'blank': True, 'null': True}

class Website(models.Model):
    """
    For a website to render, it must be added here 
    """
    domain = models.CharField(max_length=40)
    meta_desc = models.TextField(**blankfield)
    meta_key = models.TextField(**blankfield)
    notes = models.TextField(**blankfield)

    def get_index_page(self):
        """ get the index page """
        try:
            return self.website_set.select_related().filter(name='index')[0]
        except:
            return None

    def save(self, *args, **kwargs):
        self.domain = self.domain.replace('http://', '').replace('/','').replace('www','')
        super(Website, self).save(*args, **kwargs)



class WebsitePage(models.Model):
    """ 
    Represents a webpage on a particular website
    setting index to be default 
    Page Types:
      - Static Arg: This is a static page that requires an argument
      - Static: Static pages are pages with a predefined method. E.g, products
          will search the products database and return products variable.
          You can introduct new static pages with predefined methods for custom apps
      - Sub-Landing: Defines a custom subpage or landing page at the top level or url (sitename.com/subpage) - 
          this has to be a name that is not defined in as a "static" url. For example, a contact us page specific
          for the site you are making, or a landing page for marketing
      - Landing: Landing page will require 
      
    """
    PAGETYPES = (('sub-landing', 'sub-landing',), ('landing','landing',), \
        ('static', 'static',),('static-arg', 'static-arg',),)
    
    custom_blankfield = blankfield
    custom_blankfield['max_length']= 30

    website = models.ForeignKey('Website')
    title = models.CharField(max_length=30, default='')
    name = models.CharField(max_length=20, default='index')
    type = models.CharField(max_length=15, choices=PAGETYPES)
    template = models.CharField(max_length=50, blank=True, null=True)
    redirects_to = models.CharField(**custom_blankfield)

    def save(self, *args, **kwargs):
        """ 
        Parse the name and save 
        raise validation error if name is in static-pages list
        """
        self.name = self.name.lower().replace(' ', '_').replace('.','').replace('/','')
        # override index as type if name matches
        if self.name == 'index':
            self.type = 'index'
        # override title if nothing is set
        if not self.title:
            self.title = self.name
        # do not allow page names of static URLS
        if self.name in STATIC_PAGES:
            raise ValidationError('Page name cannot be in static pages: %s' % str([x for x in STATIC_PAGES]))
        super(WebsitePage, self).save(*args, **kwargs)

