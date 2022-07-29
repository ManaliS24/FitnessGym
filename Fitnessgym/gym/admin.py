from django.contrib import admin
from .models import Trainer, Course, TimeTable

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "trainer", "price", "img")


class TimeTableAdmin(admin.ModelAdmin):
    list_display = ("course", "day_of_week", "start_end_time")


class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "desc")


admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(TimeTable, TimeTableAdmin)

