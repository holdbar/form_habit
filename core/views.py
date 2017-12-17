# -*- coding: utf-8 -*-

# form_habit
# form_habit/core/views.py

from django.shortcuts import render
from core.models import Habit

__all__ = [
	"habit_list",
]

def habit_list(request):
    habits = Habit.objects.filter(owner=request.user)
    return render(request, "core/habit_list.html", {"habits": habits})
