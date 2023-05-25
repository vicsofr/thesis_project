import urllib

from rest_framework import viewsets, permissions

from company.models import Employee, Department
from company.serializers import EmployeeSerializer, DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

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


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]
