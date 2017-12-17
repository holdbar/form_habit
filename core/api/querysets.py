# -*- coding: utf-8 -*-

# form_habit
# form_habit/core/api/querysets.py

from django.db import models


__all__ = [
    "HabitQuerySet",
]


class HabitQuerySet(models.QuerySet):
    """
    Habit model queryset.
    """

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

        return self.filter(finished=True)

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

        return self.filter(finished=False)

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
        
        return self.filter(dropped=True)
        