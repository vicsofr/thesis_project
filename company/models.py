from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    director = models.OneToOneField('Employee', on_delete=models.SET_NULL, null=True, related_name='department_dir')

    def __str__(self):
        return f'Департамент "{self.name}"'


class Employee(models.Model):
    full_name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(upload_to='employee_photos', blank=True)
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.full_name
