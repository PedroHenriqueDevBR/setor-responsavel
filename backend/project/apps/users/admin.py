from django.contrib import admin
from apps.users.models import Employee, Sector, Subsidiary


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["contact", "identifier", "sector", "user"]


@admin.register(Subsidiary)
class SubsidiaryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ["name", "subsidiary"]
