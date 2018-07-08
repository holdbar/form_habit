# -*- coding: utf-8 -*-

from django.db.models import QuerySet


__all__ = [
    "UserQuerySet",
]


class UserQuerySet(QuerySet):
    """
    User model queryset.
    """

    def active(self, *args, **kwargs):
        """
        Return users with is_active == True.
        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: queryset of users with is_active == True.
        :rtype: django.db.models.query.QuerySet.
        """

        return self.filter(is_active=True)
        