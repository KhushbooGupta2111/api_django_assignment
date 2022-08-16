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
    fullcaps = request.GET.get('fullcaps','off')
    newline = request.GET.get('newline','off')
    spaceremove = request.GET.get('spaceremove','off')
    counter = request.GET.get('counter','off')
    print(djtext)
    analysed = ""
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Removed Punctuations', 'analysed_text' : analysed}

        return render(request, 'analyse.html', params)
    elif(fullcaps == "on"):
        analysed = ""
        for char in djtext:
            analysed = ""
            for char in djtext:
                analysed = analysed + char.upper()
        params = {'purpose':'Changed to Uppercase', 'analysed_text' : analysed}
        return render(request, 'analyse.html', params)
    elif(newline == "on"):
        analysed = ""
        for char in djtext:
            if char != "\n":
                analysed = analysed + char
        params = {'purpose':'Removed New Lines', 'analysed_text' : analysed}
        return render(request, 'analyse.html', params)
    elif(spaceremove == "on"):
        analysed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analysed = analysed + char
        params = {'purpose':'Removed Extra Spaces', 'analysed_text' : analysed}
        return render(request, 'analyse.html', params)
    elif(counter == "on"):
        analysed = ""
        count = 0
        for  char in djtext:
            count += 1
        analysed = count


        params = {'purpose':'Counting the number of Characters in the String ', 'analysed_text' : analysed}
        return render(request, 'analyse.html', params)
    else:
        return HttpResponse("Error")

def exl(request):
    s = '''<h2>Navigation Bar <br></h2>
    <a href="https://www.youtube.com/">Youtube</a><br><a href="https://www.youtube.com/">Youtube</a><br><a href="https://www.youtube.com/">Youtube</a><br><a href="https://www.youtube.com/">Youtube</a><br>
  '''

    return HttpResponse(s)

