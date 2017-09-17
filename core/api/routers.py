# -*- coding: utf-8 -*-

# form_habit
# form_habit/core/api/routers.py

from rest_framework.routers import DefaultRouter

from core.api.viewsets import HabitViewSet, HabitLogViewSet, UserViewSet

router = DefaultRouter()

# registering viewsets
router.register(r"habit", HabitViewSet)
router.register(r"habit-log", HabitLogViewSet)
router.register(r"user", UserViewSet)
