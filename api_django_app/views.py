from django.core.checks import templates
from django.shortcuts import render
import requests

def home(request):
    response = requests.get('https://api.covid19api.com/countries').json()
    return render(request, 'home.html',{'response':response})


