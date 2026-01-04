# from internship.wsgi import application as app
# app = application

import os
from internship.wsgi import application

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship.settings')

application = get_wsgi_application()


app = application
