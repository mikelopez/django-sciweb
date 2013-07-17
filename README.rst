Sciweb
------
Create Dynamic domain driven Affiliate Commerce sites in Django.
Uses Shopzilla publisher services for product & price comparison
You can also create custom landing pages on specific products
Add your own products or implement your own apps

http://django-sciweb.readthedocs.org

Getting Started
--------------

* Create your local_settings.py file
* Start the server

``cp local_settings.template local_settings.py``
``mkvirtualenv sciweb``
``pip install -r requirements.txt``


local_settings.py
=================

.. code-block:: python
 
    from django.conf.urls.defaults import *
    # Uncomment the next two lines to enable the admin:

    ENABLE_ADMIN = True
    DEBUG = True
    DEBUG_CRUD = True
    LOG_ON = True
    TEMPLATE_DEBUG = DEBUG

    # same as application_url_includes url value
    # hardcoded to redirect to admin - no client login implemented
    LOGIN_REDIRECT_URL = '/webadmin/yay/hooray'

    # debugtoolbar IP settings (optional)
    INTERNAL_IPS = ('127.0.0.1','localhost',)

    # set the logger to writet!


    # set dev-installed apps 
    DEV_INSTALLED_APPS = (
      #'appname',
      'lettuce.django',
      'debug_toolbar',
      'mainweb',
    )

    # add additional ccustom middleware classes
    DEV_MIDDLEWARE_CLASSES = (
        #'djangologging.middleware.LoggingMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        #'debug_logging.middleware.DebugLoggingMiddleware',
    )
      
    # enable or disable admins - uncomment and modify with your url
    if ENABLE_ADMIN:
      application_url_includes = patterns('',
        #(r'^admin/(.*)', admin.site.root),
      )
    else:
      application_url_includes = patterns('',)


    # choose the view for the root URL /
    mastersite_rooturl = patterns('',
      #url(r'^$', 'web.views.admin_redirect'),
      url(r'^robots.txt','mainweb.views.robots'),
      url(r'^$', 'mainweb.views.index', name="mainweb_index"),
      url(r'^(?P<linkname>\w+)/(?P<filtername>[\w -]+)', 'mainweb.views.index'),
      url(r'^(?P<linkname>\w+)','mainweb.views.index'),
    )

    # assuming mysql db - assuming django.db.backends.mysql
    DATABASES = {
        'test': {
            'ENGINE': 'django.db.backends.',
            'NAME': 'testdatabase',
            'HOST': '',
            'PASSWORD': 'testpassword',
            'USER': 'testuser'

        },
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'dbdata.sqlite3',
            'HOST': '',
            'PASSWORD': '',
            'USER': '',
        }
    }
    DATABASE_ENGINE = DATABASES.get('default').get('ENGINE')
    DATABASE_NAME = DATABASES.get('default').get('NAME')
    DATABASE_USER = DATABASES.get('default').get('USER')
    DATABASE_PASSWORD = DATABASES.get('default').get('PASSWORD')
    DATABASE_HOST = DATABASES.get('default').get('HOST')
    DATABASE_PORT = ''

    # dynamic shopzilla query pages (search, compare, category view
    SHOP_SEARCH = 'shopsearch'
    SHOP_COMPARE = 'shopcompare'
    SHOP_CATEGORY = 'shopcategory'

    # define the static page names that will be used in the URL
    STATIC_PAGES = ['products', 'articles' ]
    # define static pages that require an arg
    STATIC_ARG_PAGES = ['p', 'search', 'a', SHOP_SEARCH, SHOP_COMPARE, SHOP_CATEGORY]

    # optional if using django-debug-toolbar
    DEBUG_TOOLBAR_PANELS = (
        #'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        #'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )

