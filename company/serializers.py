from django.db.models import Sum
from rest_framework import serializers
from .models import Department, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    num_employees = serializers.IntegerField(source='employees.count', read_only=True)
    total_salary = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'director', 'num_employees', 'total_salary']

    def get_total_salary(self, obj):
        total_department_salary = Employee.objects.filter(department=obj.id).aggregate(sum_salary=Sum('salary'))
        return total_department_salary['sum_salary']
