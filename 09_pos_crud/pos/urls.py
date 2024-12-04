from django.urls import path

from pos import views

urlpatterns = [
    path('category/', views.category_list, name='category_list'),
    path('category/add', views.category_add, name='category_add'),
]