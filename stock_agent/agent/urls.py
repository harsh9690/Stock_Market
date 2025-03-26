from django.urls import path
from .views import fetch_stock, stock_recommendation

urlpatterns = [
    path('stock/<str:ticker>/', fetch_stock, name='fetch_stock'),
    path('recommend/<str:ticker>/', stock_recommendation, name='stock_recommendation'),
]
