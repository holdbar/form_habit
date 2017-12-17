# -*- coding: utf-8 -*-

# form_habit
# form_habit/core/api/viewsets.py

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Habit, HabitLog, User
from core.api.serializers import HabitSerializer, HabitLogSerializer, UserSerializer
from core.api.permissions import HabitPermissions, HabitLogPermissions, UserPermissions
from core.constants import GET



__all__ = [
    "HabitViewSet",
    "HabitLogViewSet",
    "UserViewSet",
]


class HabitViewSet(ModelViewSet):
    """
    Habit view set.
    """

    queryset = Habit.objects.all() 
    serializer_class = HabitSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    permission_classes = [HabitPermissions, ]
    filter_fields = ["finished", ]
    ordering_fields = ["created", "updated", ]

    def perform_create(self, serializer):
        """
        Override to set habit owner.

        :param serializer: instance of habit model serializer.
        :type serializer: core.api.serializers.HabitSerializer.
        """

        defaults = {
            "owner": self.request.user,
        }

        serializer.save(**defaults)

    @list_route(methods=[GET, ])
    def my(self, request, **kwargs):
        """
        Return only user owned habits.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=request.user.owned.all() if request.user.is_authenticated else Habit.objects.none())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @list_route(methods=[GET, ])
    def finished(self, request, **kwargs):
        """
        Return only finished habits.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=Habit.objects.finished())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @list_route(methods=[GET, ])
    def unfinished(self, request, **kwargs):
        """
        Return only unfinished habits.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=Habit.objects.unfinished())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @list_route(methods=[GET, ])
    def dropped(self, request, **kwargs):
        """
        Return only dropped habits.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=Habit.objects.dropped())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @list_route(methods=[GET, ], url_path="my/finished")
    def my__finished(self, request, **kwargs):
        """
        Return only finished user owned habits.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=request.user.owned.finished() if request.user.is_authenticated else Habit.objects.none())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @list_route(methods=[GET, ], url_path="my/unfinished")
    def my__unfinished(self, request, **kwargs):
        """
        Return only unfinished user owned groups.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=request.user.owned.unfinished() if request.user.is_authenticated else Habit.objects.none())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @list_route(methods=[GET, ], url_path="my/dropped")
    def my__dropped(self, request, **kwargs):
        """
        Return only dropped user owned groups.

        :param request: django request instance.
        :type request: django.http.request.HttpRequest.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: serialized custom queryset response.
        :rtype: rest_framework.response.Response.
        """

        queryset = self.filter_queryset(queryset=request.user.owned.dropped() if request.user.is_authenticated else Habit.objects.none())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


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
    


