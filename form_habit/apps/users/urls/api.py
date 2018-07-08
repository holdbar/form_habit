# -*- coding: utf-8 -*-

from django.urls import (
    path,
    include,
)

from form_habit.apps.users.api.routers import router


__all__ = [
    "api",
]


api = [
    path(r"api/", include(router.urls)),
]
