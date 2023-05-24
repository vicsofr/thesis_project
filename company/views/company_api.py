from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions
import urllib.parse

from company.models import Department, Employee
from company.serializers import DepartmentSerializer, EmployeeSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get a list of employees",
        permission_classes=[permissions.IsAuthenticated],
        responses={200: EmployeeSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                name='last_name',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Filter employees by last name',
                required=False,
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        """
        Get a list of employees.
        """
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new employee",
        permission_classes=[permissions.IsAuthenticated],
        request_body=EmployeeSerializer,
        responses={201: EmployeeSerializer()},
    )
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
        if last_name is not None:
            value = urllib.parse.unquote(last_name)
            queryset = queryset.filter(full_name__icontains=value)
        return queryset


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve an employee",
        permission_classes=[permissions.IsAuthenticated],
        responses={200: EmployeeSerializer()},
    )
    def get(self, request, *args, **kwargs):
        """
        Retrieve an employee.
        """
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update an employee",
        permission_classes=[permissions.IsAuthenticated],
        request_body=EmployeeSerializer,
        responses={200: EmployeeSerializer()},
    )
    def put(self, request, *args, **kwargs):
        """
        Update an employee.
        """
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete an employee",
        permission_classes=[permissions.IsAuthenticated],
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        """
        Delete an employee.
        """
        return self.destroy(request, *args, **kwargs)


class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description="Get a list of departments",
        responses={200: DepartmentSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        """
        Get a list of departments.
        """
        return self.list(request, *args, **kwargs)
