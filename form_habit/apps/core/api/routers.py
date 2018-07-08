# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter

from form_habit.apps.core.api.viewsets.habit import HabitViewSet
from form_habit.apps.core.api.viewsets.habit_log import HabitLogViewSet

router = DefaultRouter()

# registering viewsets
router.register(r"habit", HabitViewSet)
router.register(r"habit-log", HabitLogViewSet)
