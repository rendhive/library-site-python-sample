import site

if site.ENABLE_USER_SITE:
    print("Dukungan untuk site pengguna diaktifkan.")
else:
    print("Dukungan untuk site pengguna dinonaktifkan.")
# Fungsi: Memeriksa apakah dukungan untuk lokasi repositori pengguna diaktifkan.
# Kondisi: Ketika Anda memerlukan kontrol tentang penggunaan package pengguna.