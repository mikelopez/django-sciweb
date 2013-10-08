import os, sys
from django.conf import settings

PROJECT_ROOTDIR = os.path.realpath(os.path.dirname(__file__))
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

settings.configure(DEBUG=True,
                  DATABASES={
                        'default': {
                            'ENGINE': 'django.db.backends.sqlite3',
                        }
                  },
                  ROOT_URLCONF='mainweb.urls',
                  INSTALLED_APPS=('django.contrib.auth',
                                  'django.contrib.contenttypes',
                                  'django.contrib.sessions',
                                  'django.contrib.admin',
                                  'mainweb',))

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['mainweb', ])
if failures:
    sys.exit(failures)
