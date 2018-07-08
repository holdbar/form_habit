# -*- coding: utf-8 -*-


from django.urls import include, path
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token

from form_habit.apps.core.api.routers import router

__all__ = [
    "urlpatterns",
]

urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"get-api-token/", obtain_auth_token, name="get-api-token"),
    path(r"users/", include(("form_habit.apps.users.urls", "users"), namespace="users")),
    path(r"core/", include(("form_habit.apps.core.urls", "core"), namespace="core")), 
]



