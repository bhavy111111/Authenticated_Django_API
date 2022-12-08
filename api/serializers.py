from rest_framework import serializers
from api.models import Company,Employee

#create serializers
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'location', 'about','type','added_date','active']

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  =Employee
        fields = ['id', 'name','email','address','phone','about','position','company']