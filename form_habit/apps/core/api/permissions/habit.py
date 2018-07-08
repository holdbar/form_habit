# -*- coding: utf-8 -*-

# form_habit
# form_habit/core/api/permissions.py

from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)

from form_habit.apps.core.constants import (
    POST,
    DELETE,
    PATCH,
)


__all__ = [
    "HabitPermissions",
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
        :type view: form_habit.apps.core.api.viewsets.habit.HabitViewset.
        :return: permission is granted.
        :rtype: bool.
        """

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True

        if all([request.method == POST, request.user.is_authenticated(), ]):
            # Allow create habits only for authenticated users.
            return True

        if all([request.method == PATCH, request.user.is_authenticated(), ]):
            # In futures steps of flow allow user edit self owned habits.
            return True

    def has_object_permission(self, request, view, obj):
        """
        Show/edit/delete object permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: form_habit.apps.core.api.viewsets.habit.HabitViewset.
        :param obj: group model instance.
        :type obj: form_habit.apps.core.models.habit.Habit.
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
