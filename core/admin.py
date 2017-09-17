from django.contrib import admin
from core.models import Habit, HabitLog, User

# Register your models here.

admin.site.register(Habit)
admin.site.register(HabitLog)
admin.site.register(User)
