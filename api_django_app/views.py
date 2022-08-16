from django.core.checks import templates
from django.shortcuts import render
from django.http import HttpResponse
import requests
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from api_django_app.models import Department,Employees
# from api_django_app.serializers import DepartmentSerializer, EmployeeSerializer


def index(request):
    return render(request, 'index.html')
def analyse(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(djtext)
    analysed = ""
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Removed Punctuations', 'analysed_text' : analysed}

        return render(request, 'analyse.html', params)
    else:
        return HttpResponse("Error")

def exl(request):
    s = '''<h2>Navigation Bar <br></h2>
    <a href="https://www.youtube.com/">Youtube</a><br><a href="https://www.youtube.com/">Youtube</a><br><a href="https://www.youtube.com/">Youtube</a><br><a href="https://www.youtube.com/">Youtube</a><br>
  '''
    return HttpResponse(s)

# @csrf_exempt
# def departmentApi(reuqest,id=0):
#     if reuqest.method == 'GET':
#         departments = Department.objects.all()
#         departments_serializer = DepartmentSerializer(departments,many=True)
#         return JsonResponse(departments_serializer.data,safe=False)
#     elif reuqest.method == 'POST':
#         department_data = JSONParser().parse(reuqest)
#         department_serializer = DepartmentSerializer(data = department_data)
#         if department_serializer.is_valid():
#             department_serializer.save()
#             return JsonResponse("Added Successfully", safe = False)
#           return JsonResponse("Failed to Add", safe = False)
#     elif reuqest.method == 'PUT':
#         department_data = JSONParser().parse(reuqest)
#         department = Department.objects.get(DepartmentId = department_data['DepartmentId'])
#         department_serializer = DepartmentSerializer(department,data = department_data)
#         if department_serializer.is_valid():
#             department_serializer.save()
#             return JsonResponse("Update Successfully", safe = False)
#         return JsonResponse("Failed to Update")
#     elif reuqest.method == 'DELETE':
#         department = Department.objects.get(DepartmentId = id)
#         department.delete()
#         return JsonResponse("Deleted Successfully" ,safe = True)
#
#
#
