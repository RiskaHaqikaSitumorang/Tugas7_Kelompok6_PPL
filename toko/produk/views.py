from django.shortcuts import render
from django.http import HttpResponse
from .models import Produk

# Data dummy (sementara sebelum database siap)
produk_list = [
    {
        'id': 1,
        'nama': 'Laptop ASUS X441UA',
        'harga': 6500000,
        'deskripsi': 'Laptop dengan prosesor Intel Core i5 dan RAM 8GB',
        'stok': 10
    },
    {
        'id': 2,
        'nama': 'Smartphone Samsung Galaxy A51',
        'harga': 4200000,
        'deskripsi': 'Smartphone dengan kamera 48MP dan baterai 4000mAh',
        'stok': 15
    },
    {
        'id': 3,
        'nama': 'TV LED 32 Inch Sharp',
        'harga': 2800000,
        'deskripsi': 'TV LED dengan resolusi HD dan fitur Smart TV',
        'stok': 8
    },
    {
        'id': 4,
        'nama': 'Kulkas 2 Pintu LG',
        'harga': 5500000,
        'deskripsi': 'Kulkas hemat energi dengan teknologi Inverter',
        'stok': 5
    }
]

def home(request):
    return render(request, 'produk/home.html')

def daftar_produk(request):
    context = {
        'produk_list': produk_list,
        'title': 'Daftar Produk'
    }
    return render(request, 'produk/daftar_produk.html', context)

def produk_detail(request, produk_id):
    produk = next((p for p in produk_list if p['id'] == produk_id), None)
    if produk:
        context = {
            'produk': produk,
            'title': f"Detail {produk['nama']}"
        }
        return render(request, 'produk/produk_detail.html', context)
    else:
        return HttpResponse("Produk tidak ditemukan", status=404)

def kontak(request):
    return render(request, 'produk/kontak.html')