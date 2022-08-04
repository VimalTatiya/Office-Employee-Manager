from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.index , name='index'),
    path('view_employees', views.view_employees , name='view_employees'),
    path('add_employee', views.add_employee , name='add_employee'),
    path('remove_employee', views.remove_employee , name='remove_employee'),
    path('remove_employee/<int:emp_id>', views.remove_employee , name='remove_employee'),
    path('filter_employees', views.filter_employees , name='filter_employees'),
]