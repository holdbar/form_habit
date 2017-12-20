# -*- coding: utf-8 -*-

# form_habit
# form_habit/core/models.py

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from core.api.managers import HabitManager

__all__ = [
    "Habit",
    "HabitLog",
    "User",
]

class Habit(models.Model):
    """
    User habit model.
    """

    name = models.CharField(verbose_name=_("name"), max_length=256, db_index=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("owner"), db_index=True, related_name="owned")
    finished = models.BooleanField(verbose_name=_("finished"), db_index=True, default=False)
    dropped = models.BooleanField(verbose_name=_("dropped"), db_index=True, default=False)
    created = models.DateTimeField(verbose_name=_("habit creation date and time"), blank=True, null=True, db_index=True, auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("formed/dropped date and ime"), blank=True, null=True, db_index=True, auto_now=True)

    objects = HabitManager()

    class Meta:

        app_label = "core"
        verbose_name = _("habit")
        verbose_name_plural = _("habits")
        unique_together = ["name", "owner",]


    def __unicode__(self):

        return self.name

    def __str__(self):

        return self.__unicode__()


class HabitLog(models.Model):
    """
    User habit forming log.
    """

    habit = models.ForeignKey("core.Habit", verbose_name=_("habit"), db_index=True, related_name="logs")
    created = models.DateTimeField(verbose_name=_("creation date and time"), blank=True, null=True, db_index=True, auto_now_add=True)


    class Meta:

        app_label = "core"
        verbose_name = _("habit log")
        verbose_name_plural = _("habit logs")
        ordering = ["-created", ]

    def __unicode__(self):

        return self.habit

    def __str__(self):

        return self.__unicode__()


class User(AbstractUser):
    """
    User model.
    """


    class Meta:

        app_label = "core"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __unicode__(self):

        return self.username

    def __str__(self):

        return self.__unicode__()
