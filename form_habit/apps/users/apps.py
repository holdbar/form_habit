# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

__all__ = [
    "Config",
]

class Config(AppConfig):
    """
    Users app config.
    """

    name = "form_habit.apps.users"
    verbose_name = _("Users")
