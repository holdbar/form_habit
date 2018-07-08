# -*- coding: utf-8 -*-

from django.contrib.auth.models import UserManager as AbstractUserManager
from django.utils import timezone
from django.conf import settings

from form_habit.apps.users.querysets.user import UserQuerySet


__all__ = [
    "UserManager",
]


class UserManager(AbstractUserManager):
    """
    User model manager.
    """

    def get_queryset(self, *args, **kwargs):
        """
        Override to return custom queryset.
        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: User model queryset instance.
        :rtype: form_habit.apps.users.querysets.user.UserQuerySet.
        """

        return UserQuerySet(self.model, using=self._db)

    def _create_user(self, username, email=None, password=None, **kwargs):
        """
        Create new user.
        :param username: username.
        :type username: unicode.
        :param email: user email.
        :type email: unicode.
        :param password: user password.
        :type password: unicode.
        :type type: int.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: created user instance.
        :rtype: fotm_habit.apps.user.models.user.User.
        """

        email = UserManager.normalize_email(email)
        user = self.model(username=email, email=email, is_active=True, date_joined=timezone.now(), **kwargs)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email=None, password=None, **kwargs):
        """
        Create new user.
        :param username: username.
        :type username: unicode.
        :param email: user email.
        :type email: unicode.
        :param password: user password.
        :type password: unicode.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: created user instance.
        :rtype: form_habit.apps.user.models.user.User.
        """

        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)

        return self._create_user(username, email, password, **kwargs)

    def create_superuser(self, username, email, password, **kwargs):
        """
        Create new superuser.
        :param username: username.
        :type username: unicode.
        :param email: user email.
        :type email: unicode.
        :param password: user password.
        :type password: unicode.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: created user instance.
        :rtype: form_habit.apps.user.models.user.User.
        """

        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("is_staff") is not True:

            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:

            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **kwargs)

    def create(self, *args, **kwargs):
        """
        Override to create user codes model instance and send confirmation email.
        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: created user instance.
        :rtype: form_habit.apps.user.models.user.User.
        """


        user = super(UserManager, self).create(**kwargs)

        return user

    def active(self, *args, **kwargs):
        """
        Return active users.
        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: queryset of users with is_active == True.
        :rtype: form_habit.apps.users.querysets.user.UserQuerySet.
        """

        return self.get_queryset().active(*args, **kwargs)
