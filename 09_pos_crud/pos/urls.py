from django.urls import path

from pos import views

urlpatterns = [
    path('category/', views.category_list, name='category_list'),
    path('category/add', views.category_add, name='category_add'),
    path('category/<int:pk>/edit', views.category_edit, name='category_edit'),
    path('category/<int:pk>/delete', views.category_delete, name='category_delete'),

    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:id>/update/', views.update_product, name='update_product'),
    path('products/<int:id>/delete/', views.delete_product, name='delete_product'),

    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.create_customer, name='create_customer'),
    path('customers/<int:id>/update/', views.update_customer, name='update_customer'),
    path('customers/<int:id>/delete/', views.delete_customer, name='delete_customer'),
]