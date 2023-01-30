from django.contrib import admin

# Register your models here.
from .models import Employee, Job

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'joining_date']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name'] 