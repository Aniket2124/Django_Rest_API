from django.contrib import admin
from .models import Employee


@admin.register(Employee)
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'emp_id', 'salary', 'city']
