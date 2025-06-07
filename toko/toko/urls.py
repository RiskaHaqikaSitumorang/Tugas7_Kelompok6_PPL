# toko/urls.py (file utama)
from django.contrib import admin
from django.urls import path, include
from produk import views  # JANGAN import views dari project utama

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('produk/', include('produk.urls')),  # Pastikan ini ada
    path('kontak/', views.kontak, name='kontak'),
]