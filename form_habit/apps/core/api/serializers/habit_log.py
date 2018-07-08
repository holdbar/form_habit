# -*- coding: utf-8 -*-

from rest_framework import serializers
from form_habit.apps.core.models.habit_log import HabitLog


__all__ = [
    "HabitLogSerializer",
]

class HabitLogSerializer(serializers.ModelSerializer):
    """
    HabitLog model serializer.
    """

    class Meta:

        model = HabitLog
        read_only_fields = [
            "created",
            ""
        ]
        extra_kwargs = {
            "url": {"view_name": "core:habitlog-detail", },
        }
        fields = [
            "id",
            "name",
            "created",
            "url",
        ]
