# -*- coding: utf-8 -*-

from django.db import models

from form_habit.apps.core.querysets.habit import HabitQuerySet


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
        :rtype: form_habit.apps.core.querysets.habit.HabitQuerySet.
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
