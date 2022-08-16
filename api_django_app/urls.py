from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('analyze/', views.analyze),
    path('ex1/', views.ex1),
]