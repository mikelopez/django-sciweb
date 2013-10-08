import os, sys
from django.conf import settings

PROJECT_ROOTDIR = os.path.realpath(os.path.dirname(__file__))
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_PATH, ''))
sys.path.insert(1, os.path.join(PROJECT_PATH, 'apps'))
settings.configure(DEBUG=True,
                  DATABASES={
                        'default': {
                            'ENGINE': 'django.db.backends.sqlite3',
                        }
                  },
                  ROOT_URLCONF='sciweb.apps.mainweb.urls',
                  INSTALLED_APPS=('django.contrib.auth',
                                  'django.contrib.contenttypes',
                                  'django.contrib.sessions',
                                  'django.contrib.admin',
                                  'sciweb.apps.mainweb',))

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['sciweb.apps.mainweb', ])
if failures:
    sys.exit(failures)
