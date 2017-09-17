from django.shortcuts import render
from core.models import Habit

# Create your views here.

def habit_list(request):
    habits = Habit.objects.filter(owner=request.user)
    return render(request, "core/habit_list.html", {"habits": habits})
