from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('create/', views.create_employee, name='create_employee'),
    # ... URL patterns lainnya ...
    path('departments/', views.department_list, name='department_list'),
    path('departments/create/', views.create_department, name='create_department'),
    path('departments/<int:pk>/update/', views.update_department, name='update_department'),
    path('departments/<int:pk>/delete/', views.delete_department, name='delete_department'),
]