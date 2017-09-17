from django.conf.urls import url, include
from core import views
from core.api.viewsets import HabitViewSet



urlpatterns = [
    url(r"^$", views.habit_list, name='habit_list'),
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
    url(r"^api/habit/my/finished\.(?P<format>[a-z0-9]+)/?$", habit__my__finished, name="habit--my--finished"),
    url(r"^api/habit/my/finished/$", habit__my__finished, name="ghabit--my--finished"),
    url(r"^api/habit/my/unfinished\.(?P<format>[a-z0-9]+)/?$", habit__my__unfinished, name="habit--my--unfinished"),
    url(r"^api/habit/my/unfinished/$", habit__my__unfinished, name="habit--my--unfinished"),
    url(r"^api/habit/my/dropped\.(?P<format>[a-z0-9]+)/?$", habit__my__dropped, name="habit--my--dropped"),
    url(r"^api/habit/my/unfinished/$", habit__my__dropped, name="habit--my--dropped"),
]
