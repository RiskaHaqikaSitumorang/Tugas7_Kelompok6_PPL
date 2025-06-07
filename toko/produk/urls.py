# produk/urls.py
from django.urls import path
from . import views  # Impor dari app saat ini

urlpatterns = [
    path('', views.daftar_produk, name='daftar_produk'),
    path('<int:produk_id>/', views.produk_detail, name='produk_detail'),
]