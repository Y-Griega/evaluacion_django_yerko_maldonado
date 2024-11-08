"""
WSGI config for evaluacion2_django_yerko_maldonado project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evaluacion2_django_yerko_maldonado.settings')

application = get_wsgi_application()
