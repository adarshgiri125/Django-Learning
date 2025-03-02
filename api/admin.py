from django.contrib import admin

# Register your models here.
from .models import Company , Employee

class Companyadmin(admin.ModelAdmin):
    list_display = ('Company_id','Company_name')

class Employeeadmin(admin.ModelAdmin):
    list_display = ('emp_id','name')



admin.site.register(Company, Companyadmin)
admin.site.register(Employee, Employeeadmin)