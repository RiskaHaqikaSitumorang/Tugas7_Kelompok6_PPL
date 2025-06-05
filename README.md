# Tugas7_Kelompok6_PPL

# Toko Online Katalog Produk

![Django](https://img.shields.io/badge/Django-3.2-green)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Contributors](https://img.shields.io/badge/contributors-3-orange)

Website katalog produk sederhana dengan Django untuk menampilkan daftar produk, detail produk, dan halaman kontak.

## 📋 Daftar Isi
- [Fitur Utama](#-fitur-utama)
- [Struktur Project](#-struktur-project)
- [Panduan Instalasi](#-panduan-instalasi)
- [Cara Penggunaan](#-cara-penggunaan)
- [Kontributor](#-kontributor)
- [Lisensi](#-lisensi)

## ✨ Fitur Utama
✅ Menampilkan daftar produk  
✅ Halaman detail produk lengkap  
✅ Halaman kontak dengan form  
✅ Desain responsive  
✅ Database SQLite  
✅ Function-based views  

## 📁 Struktur Project
```
toko/
├── produk/
│   ├── migrations/
│   ├── templates/
│   │   └── produk/
│   │       ├── daftar_produk.html
│   │       ├── home.html
│   │       ├── kontak.html
│   │       └── produk_detail.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── toko/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

## 🛠 Panduan Instalasi
1. **Clone repository**:
   ```bash
   git clone [https://github.com/username/repo.git](https://github.com/RiskaHaqikaSitumorang/Tugas8_Kelompok6_PPL.git)
   cd toko
   ```

2. **Setup environment**:
   ```bash
   python -m venv venv
   # Linux/Mac
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django
   ```

4. **Setup database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Jalankan server**:
   ```bash
   python manage.py runserver
   ```

6. **Akses aplikasi**:
   ```
   http://localhost:8000
   ```

## 🖥 Cara Penggunaan
| Halaman | URL | Deskripsi |
|---------|-----|-----------|
| Home | `/` | Halaman utama |
| Daftar Produk | `/produk/` | Menampilkan semua produk |
| Detail Produk | `/produk/<id>/` | Detail produk spesifik |
| Kontak | `/kontak/` | Form kontak dan informasi |

## 👥 Kontributor

| Nama | NPM | 
|------|-----|
| Berliani Utami | 2208107010082 |
| Raihan Firyal | 2208107010084 |
| Riska Haqika Situmorang | 2208107010086 |
## 📜 Lisensi
MIT License © 2025 Kelompok 6 PPL

