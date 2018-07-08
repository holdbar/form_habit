# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from django.contrib.sessions.models import Session
from rest_framework.authtoken.models import Token

from form_habit.apps.users.managers.user import UserManager

__all__ = [
    "User",
]

class User(AbstractUser):
    """
    User model.
    """

    id = models.IntegerField(primary_key=True, editable=False, verbose_name=_("ID"))

    FIELDS = ["id",]

    objects = UserManager()

    class Meta:

        app_label = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")


    def __str__(self):

        return getattr(self, self.USERNAME_FIELD)

    def kick(self):
        """
        Clear all user sessions and API keys (logout from all logged in devices).
        """

        Token.objects.filter(user=self).delete()  # delete all user API keys

        sessions = Session.objects.all()

        for session in sessions:
            if session.get_decoded().get("_auth_user_id") == self.pk:
                session.delete()
                