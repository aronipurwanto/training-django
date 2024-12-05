from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet
from .views_trx import TransactionViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'trx', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

