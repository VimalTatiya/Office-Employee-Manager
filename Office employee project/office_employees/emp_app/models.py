from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)
    class Meta:
            verbose_name = 'Department'
            verbose_name_plural = 'Departments'
    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)
    class Meta:
            verbose_name = 'Role'
            verbose_name_plural = 'Roles'
    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    class Meta:
            verbose_name = 'Employee'
            verbose_name_plural = 'Employees'

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)