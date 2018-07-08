# -*- coding: utf-8 -*-

from django.contrib import admin

from form_habit.apps.core.models.habit import Habit
from form_habit.apps.core.models.habit_log import HabitLog

admin.site.register(Habit)
admin.site.register(HabitLog)
