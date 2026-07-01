import site

def summarize_configuration():
    print("Ringkasan konfigurasi saat ini:")
    site_packages = site.getsitepackages()
    for path in site_packages:
        print(f"- Paket lanjutan berada di {path}")

summarize_configuration()
# Fungsi: Menampilkan ringkasan pengaturan semua jalur dan informasi penting.
# Kondisi: Ketika Anda ingin memberikan gambaran umum tentang konfigurasi Python.