# -*- coding: utf-8 -*-

# form_habit
# form_habit/core/api/permissions.py

from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)
from rest_framework.compat import is_authenticated

from core.constants import (
    POST,
    DELETE,
    PATCH,
)


__all__ = [
    "HabitPermissions",
    "HabitLogPermissions",
    "UserPermissions",
]


class HabitPermissions(BasePermission):
    """
    Habit permissions.
    """

    def has_permission(self, request, view):
        """
        List/create objects permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: core.api.viewsets.HabitViewset.
        :return: permission is granted.
        :rtype: bool.
        """

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True

        if all([request.method == POST, is_authenticated(request.user), ]):
            # Allow create habits only for authenticated users.
            return True

        if all([request.method == PATCH, is_authenticated(request.user), ]):
            # In futures steps of flow allow user edit self owned habits.
            return True

    def has_object_permission(self, request, view, obj):
        """
        Show/edit/delete object permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: core.api.viewsets.HabitViewset.
        :param obj: group model instance.
        :type obj: core.models.Habit.
        :return: permission is granted.
        :rtype: bool.
        """

        if all([request.method == PATCH, obj.owner == request.user, ]):
            # Allow only owner edit habits.
            return True

        if request.method == DELETE:
            # Disallow delete habits by anyone.
            return False

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True


class HabitLogPermissions(BasePermission):
    """
    HabitLog permissions.
    """

    def has_permission(self, request, view):
        """
        List/create objects permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: core.api.viewsets.HabitViewset.
        :return: permission is granted.
        :rtype: bool.
        """

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True

        if all([request.method == POST, is_authenticated(request.user), ]):
            # Allow create HabbitLog data only for authenticated users.
            return True

        if all([request.method == PATCH, is_authenticated(request.user), ]):
            # Disallow edit HabitLog data by anyone.
            return False

    def has_object_permission(self, request, view, obj):
        """
        Show/edit/delete object permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: core.api.viewsets.HabitViewset.
        :param obj: group model instance.
        :type obj: core.models.Habit.
        :return: permission is granted.
        :rtype: bool.
        """


        if request.method == DELETE:
            # Disallow delete HabitLog data by anyone.
            return False

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True


class UserPermissions(BasePermission):
    """
    User permissions.
    """

    def has_permission(self, request, view):
        """
        List/create objects permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: core.api.viewsets.UserViewset.
        :return: permission is granted.
        :rtype: bool.
        """

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True

        if request.method == POST:
            # Allow create users.
            return True

        if request.method == PATCH:
            # In futures steps of flow allow user edit self.
            return True

    def has_object_permission(self, request, view, obj):
        """
        Show/edit/delete object permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: core.api.viewsets.UserViewset.
        :param obj: user model instance.
        :type obj: core.models.User.
        :return: permission is granted.
        :rtype: bool.
        """

        if obj == request.user:
            # Allow only owner edit objects.
            return True

        if request.method == DELETE:
            # Disallow delete users by anyone.
            return False

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True
