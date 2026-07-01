import site
import os

config_file = os.path.join(site.getusersitepackages(), 'config.py')
if os.path.isfile(config_file):
    print("File konfigurasi ditemukan.")
else:
    print("File konfigurasi tidak ditemukan.")
# Fungsi: Memeriksa apakah file konfigurasi tertentu ada di situs pengguna.
# Kondisi: Ketika Anda ingin memvalidasi ketersediaan konfigurasi di direktori pengguna.