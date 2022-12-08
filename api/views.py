from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
#Django rest provides a class based views (Model View Set) 

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #Detail = True means you have to pass primary Key
    #companies/1/employees -  It will get total employees of company object
    @action(detail = True , methods = ['get'])
    def employees(self,request,pk=None):
        try:
            #print("get employees of ",pk=None,"company")
            company = Company.objects.get(pk=pk)
            emp=Employee.objects.filter(company=company)
            emp_serializer = EmployeeSerializer(emp,many=True,context={'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            return Response({
                'message':'Object doesnt exist'
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer