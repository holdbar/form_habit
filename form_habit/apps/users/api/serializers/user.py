# -*- coding: utf-8 -*-

# form_habit
# form_habit/core/api/serializers.py

from rest_framework import serializers
from form_habit.apps.users.models.user import User


__all__ = [
    "UserSerializer",
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


