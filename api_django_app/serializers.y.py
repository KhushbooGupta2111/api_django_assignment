from rest_framework import serializers
from api_django_app.models import Department,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('DepartmentId','DepartmentName')

    class EmployeeSerialzer(serializers.ModelSerializer):
        class Meta:
            model = Employees
            fields = ('EmployeeId', 'EmployeeName','Departments','PhotoFileName')