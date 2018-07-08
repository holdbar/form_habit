# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = [
    "HabitLog",
]

class HabitLog(models.Model):
    """
    User habit forming log.
    """

    id = models.IntegerField(primary_key=True, editable=False, verbose_name=_("ID"))
    habit = models.ForeignKey("core.Habit", verbose_name=_("habit"), db_index=True, related_name="logs", on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name=_("creation date and time"), blank=True, null=True, db_index=True, auto_now_add=True)


    class Meta:

        app_label = "core"
        verbose_name = _("habit log")
        verbose_name_plural = _("habit logs")
        ordering = ["-created", ]

    def __str__(self):

        return self.habit
