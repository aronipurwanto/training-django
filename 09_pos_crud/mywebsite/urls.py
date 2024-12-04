from django.contrib import admin
from django.urls import path, re_path, include

from mywebsite import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^home/', views.index),
    path('admin/', admin.site.urls),
    path('pos/', include('pos.urls')),
]
