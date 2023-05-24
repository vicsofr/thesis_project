from django.urls import path
from company.views.company_api import (
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView,
    DepartmentListView,
)

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-retrieve-update-destroy'),
    path('departments/', DepartmentListView.as_view(), name='department-list'),
]
