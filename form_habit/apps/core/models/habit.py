# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from form_habit.apps.core.managers.habit import HabitManager

__all__ = [
    "Habit",
]

class Habit(models.Model):
    """
    User habit model.
    """

    id = models.IntegerField(primary_key=True, editable=False, verbose_name=_("ID"))
    name = models.CharField(verbose_name=_("name"), max_length=256, db_index=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("owner"), db_index=True, related_name="owned", on_delete=models.CASCADE)
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


    def __str__(self):

        return self.name

