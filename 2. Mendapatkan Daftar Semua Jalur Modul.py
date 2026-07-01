import site

paths = site.getsitepackages()
print("Daftar jalur modul:")
for path in paths:
    print(path)
# Fungsi: Mendapatkan daftar semua jalur modul untuk pemrograman Python.
# Kondisi: Ketika Anda ingin mengetahui lokasi tempat modul Python berada.