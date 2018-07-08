# -*- coding: utf-8 -*-

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
    "HabitLogPermissions",
]

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
        :type view: form_habit.apps.core.api.viewsets.habit_log.HabitLogViewset.
        :return: permission is granted.
        :rtype: bool.
        """

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True

        if all([request.method == POST, request.user.is_authenticated(), ]):
            # Allow create HabbitLog data only for authenticated users.
            return True

        if all([request.method == PATCH, request.user.is_authenticated(), ]):
            # Disallow edit HabitLog data by anyone.
            return False

    def has_object_permission(self, request, view, obj):
        """
        Show/edit/delete object permission.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param view: view set.
        :type view: form_habit.apps.core.api.viewsets.habit_log.HabitLogViewset.
        :param obj: group model instance.
        :type obj: form_habit.apps.core.models.habit_log.HabitLog.
        :return: permission is granted.
        :rtype: bool.
        """


        if request.method == DELETE:
            # Disallow delete HabitLog data by anyone.
            return False

        if request.method in SAFE_METHODS:
            # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
            return True
