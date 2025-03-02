from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, get_emp_by_id

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)

router.register(r'employee', EmployeeViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('employee/company/<int:company_id>/',get_emp_by_id,name = 'get_emp_by_id')
]