# -*- coding: utf-8 -*-

from rest_framework import serializers
from form_habit.apps.core.models.habit import Habit


__all__ = [
    "HabitSerializer",
]

class HabitSerializer(serializers.ModelSerializer):
    """
    Habit model serializer.
    """

    class Meta:

        model = Habit
        read_only_fields = [
            "created",
            "updated",
            "finished",
        ]
        extra_kwargs = {
            "url": {"view_name": "core:habit-detail", },
        }
        fields = [
            "id",
            "name",
            "owner",
            "finished",
            "dropped",
            "created",
            "updated",
            "url",
        ]
