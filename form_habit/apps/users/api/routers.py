# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter

from form_habit.apps.users.api.viewsets.user import UserViewSet


router = DefaultRouter()

# registering viewsets
router.register(r"user", UserViewSet)
