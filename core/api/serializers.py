# -*- coding: utf-8 -*-

# form_habit
# form_habit/core/api/serializers.py

from rest_framework import serializers
from core.models import Habit, HabitLog, User


__all__ = [
    "HabitSerializer",
    "HabitLogSerializer",
    "UserSerializer",
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


class UserSerializer(serializers.ModelSerializer):
    """
    User model serializer.
    """

    class Meta:

        model = User
        read_only_fields = [
            "is_staff",
            "is_superuser",
            "is_active",
            "date_joined",
        ]
        extra_kwargs = {
            "url": {"view_name": "core:user-detail", },
            model.USERNAME_FIELD: {"required": True, },
            "email": {"required": True, },
            "password": {"write_only": True},
        }
        fields = [
            "id",
            "is_active",
            "date_joined",
            model.USERNAME_FIELD,
            "email",
            "password",
            "url",
        ]


