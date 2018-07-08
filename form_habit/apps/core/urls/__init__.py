# -*- coding: utf-8 -*-

from form_habit.apps.core.urls.api import api

__all__ = [
    "urlpatterns",
]


urlpatterns = []
# merge urlpatterns
urlpatterns += api
