from django.shortcuts import render
from rest_framework import viewsets
from .serialization import CompanySerializer, EmployeeSerializer
from .models import Company, Employee
from rest_framework.decorators import api_view
from rest_framework.response import Response
 

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@api_view(['GET'])
def get_emp_by_id(request,company_id):
    try :
        employee = Employee.objects.filter(company_id = company_id)
        serializer = EmployeeSerializer(employee, many = True,context={'request': request})

        return Response(serializer.data)
    
    except Company.DoesNotExist:
          return Response({"error": "company not found"}, status = 404)
          
# @api_view(['GET'])
# def get_companies(request):
#     companies = Company.objects.all()
#     serializer = CompanySerializer(companies, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def post_companies(request):
#     serializer = CompanySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)  # Fixed from serializer.error


