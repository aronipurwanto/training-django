from django.urls import path

from pos import views

urlpatterns = [
    path('category/', views.category_list, name='category_list'),
    path('category/add', views.category_add, name='category_add'),
    path('category/<int:pk>/edit', views.category_edit, name='category_edit'),
    path('category/<int:pk>/delete', views.category_delete, name='category_delete'),
]