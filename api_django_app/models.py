from django.db import models

class Department(models.Model):
    DepartmentId = models.AutoField(primary_keys = True)
    DepartmentName = models.AutoField(max_length = 500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key = True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CarField(max_length = 500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.Charfield(max_length=500)