from rest_framework.routers import DefaultRouter

from company.views.company_api import EmployeeViewSet, DepartmentViewSet


router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'departments', DepartmentViewSet, basename='department')
urlpatterns = router.urls
