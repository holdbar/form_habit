# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

__all__ = [
    "CoreConfig",
]

class CoreConfig(AppConfig):
    """
    Core app config.
    """

    name = "form_habit.apps.core"
    verbose_name = _("Core")
