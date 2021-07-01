"""
WSGI config for monsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/skillsindatascience/skillsindatascience.pythonanywhere.com'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monsite.settings')
#os.environ['DJANGO_SETTINGS_MODULE'] = 'monsite.settings'
application = StaticFilesHandler(get_wsgi_application())
#application = get_wsgi_application()
