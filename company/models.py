from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    director = models.OneToOneField('Employee', on_delete=models.SET_NULL, null=True, related_name='department_dir')


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='employee_photos')
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
