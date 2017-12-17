# -*- coding: utf-8 -*-

# form_habit
# form_habit/form_habit/wsgi.py

"""
WSGI config for form_habit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "form_habit.settings")

application = get_wsgi_application()
