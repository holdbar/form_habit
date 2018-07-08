# -*- coding: utf-8 -*-

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from form_habit.apps.users.models.user import User
from form_habit.apps.users.api.serializers.user import UserSerializer
from form_habit.apps.users.api.permissions.user import UserPermissions
from form_habit.apps.users.constants import GET


__all__ = [
    "UserViewSet",
]

class UserViewSet(ModelViewSet):
    """
    User view set.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    permission_classes = [UserPermissions, ]
    filter_fields = ["username", ]
    ordering_fields = ["id", ]
    


