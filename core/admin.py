# -*- coding: utf-8 -*-

# form_habit
# form_habit/core/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import Habit, HabitLog, User

# Register your models here.

admin.site.register(Habit)
admin.site.register(HabitLog)
admin.site.register(User, UserAdmin)
