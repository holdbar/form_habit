# -*- coding: utf-8 -*-

# form_habit
# form_habit/core/api/managers.py

from __future__ import unicode_literals

from django.db import models

from core.api.querysets import HabitQuerySet


__all__ = [
    "HabitManager",
]


class HabitManager(models.Manager):
    """
    Habit model manager.
    """

    def get_queryset(self):
        """
        Override to return custom queryset.

        :return: Habit model queryset instance.
        :rtype: mk42.apps.core.querysets.group.GroupQuerySet.
        """

        return HabitQuerySet(self.model, using=self._db)

    def finished(self, *args, **kwargs):
        """
        Return finished habits.

        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: queryset with finished habits.
        :rtype: django.db.models.query.QuerySet.
        """

        return self.get_queryset().finished(*args, **kwargs)

    def unfinished(self, *args, **kwargs):
        """
        Return unfinished habits.

        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: queryset with unfinished habits.
        :rtype: django.db.models.query.QuerySet.
        """

        return self.get_queryset().unfinished(*args, **kwargs)

    def dropped(self, *args, **kwargs):
        """
        Return dropped habits.

        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: queryset with dropped habits.
        :rtype: django.db.models.query.QuerySet.
        """

        return self.get_queryset().dropped(*args, **kwargs)
