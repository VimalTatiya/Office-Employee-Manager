from django.contrib import admin
from emp_app.models import Department
from emp_app.models import Role
from emp_app.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    fields=(('first_name' , 'last_name'), ('dept' , 'role'),('salary' , 'bonus'), ('hire_date') , ('phone'))
    list_display = ('first_name', 'dept', 'role')
    empty_value_display = '-empty-'
    list_filter = ('dept', 'role')



admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee , EmployeeAdmin)
