from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('analyse/', views.analyse),
    path('exl/', views.exl),
]