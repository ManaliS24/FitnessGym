from django.contrib import admin
from .models import Plan, PlanMembers

# Register your models here.


class PlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

class PlanMembersAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "plan_name", "gender")


admin.site.register(Plan, PlanAdmin)
admin.site.register(PlanMembers, PlanMembersAdmin)

