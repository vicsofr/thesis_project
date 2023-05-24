from rest_framework import generics, permissions
import urllib.parse

from company.models import Department, Employee
from company.serializers import DepartmentSerializer, EmployeeSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Get a list of employees.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create a new employee.
        """
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        """
        Filter queryset by string contained in full_name
        """
        queryset = Employee.objects.all()
        last_name = self.request.query_params.get('last_name', None)
        department_id = self.request.query_params.get('department_id', None)
        if last_name is not None:
            value = urllib.parse.unquote(last_name)
            queryset = queryset.filter(full_name__icontains=value)
        if department_id is not None:
            queryset = queryset.filter(department=department_id)
        return queryset


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Retrieve an employee.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Update an employee.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete an employee.
        """
        return self.destroy(request, *args, **kwargs)


class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        """
        Get a list of departments.
        """
        return self.list(request, *args, **kwargs)
