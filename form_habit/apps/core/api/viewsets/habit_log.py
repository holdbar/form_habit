# -*- coding: utf-8 -*-

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from form_habit.apps.core.models.habit_log import HabitLog
from form_habit.apps.core.api.serializers.habit_log import HabitLogSerializer
from form_habit.apps.core.api.permissions.habit_log import HabitLogPermissions
from form_habit.apps.core.constants import GET


__all__ = [
    "HabitLogViewSet",
]

class HabitLogViewSet(ModelViewSet):
    """
    HabitLog view set.
    """

    queryset = HabitLog.objects.all()
    serializer_class = HabitLogSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    permission_classes = [HabitLogPermissions, ]
    filter_fields = ["habit", ]
    ordering_fields = ["created", ]
