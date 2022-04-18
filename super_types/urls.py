from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:pk>/', views.super_types_list)
]