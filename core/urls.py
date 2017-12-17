# -*- coding: utf-8 -*-

# form_habit
# form_habit/core/urls.py

from django.conf.urls import url, include
from core import views as core_views
from core.api.viewsets import HabitViewSet

from rest_framework.authtoken import views


urlpatterns = [
    url(r"^$", core_views.habit_list, name='habit_list'),
    url(r'^api-token-auth/', views.obtain_auth_token),
]

__all__ = [
    "api"
]

# custom endpoints
# habit
habit__my__finished = HabitViewSet.as_view({"get": "my__finished"})
habit__my__unfinished = HabitViewSet.as_view({"get": "my__unfinished"})
habit__my__dropped = HabitViewSet.as_view({"get": "my__dropped"})

api = [
    url(r"^api/habit/my/finished\.(?P<format>[a-z0-9]+)/?$", habit__my__finished, name="habit/my/finished"),
    url(r"^api/habit/my/finished/$", habit__my__finished, name="habit/my/finished"),
    url(r"^api/habit/my/unfinished\.(?P<format>[a-z0-9]+)/?$", habit__my__unfinished, name="habit/my/unfinished"),
    url(r"^api/habit/my/unfinished/$", habit__my__unfinished, name="habit/my/unfinished"),
    url(r"^api/habit/my/dropped\.(?P<format>[a-z0-9]+)/?$", habit__my__dropped, name="habit/my/dropped"),
    url(r"^api/habit/my/unfinished/$", habit__my__dropped, name="habit/my/dropped"),
]
