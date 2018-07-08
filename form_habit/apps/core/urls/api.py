# -*- coding: utf-8 -*-

from django.urls import re_path, include
from form_habit.apps.core.api.viewsets.habit import HabitViewSet

__all__ = [
    "api"
]

# custom endpoints
# habit
habit__my__finished = HabitViewSet.as_view({"get": "my__finished"})
habit__my__unfinished = HabitViewSet.as_view({"get": "my__unfinished"})
habit__my__dropped = HabitViewSet.as_view({"get": "my__dropped"})

api = [
    re_path(r"^api/habit/my/finished\.(?P<format>[a-z0-9]+)/?$", habit__my__finished, name="habit/my/finished"),
    re_path(r"^api/habit/my/finished/$", habit__my__finished, name="habit/my/finished"),
    re_path(r"^api/habit/my/unfinished\.(?P<format>[a-z0-9]+)/?$", habit__my__unfinished, name="habit/my/unfinished"),
    re_path(r"^api/habit/my/unfinished/$", habit__my__unfinished, name="habit/my/unfinished"),
    re_path(r"^api/habit/my/dropped\.(?P<format>[a-z0-9]+)/?$", habit__my__dropped, name="habit/my/dropped"),
    re_path(r"^api/habit/my/unfinished/$", habit__my__dropped, name="habit/my/dropped"),
]
