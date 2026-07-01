import site

def list_licenses():
    site_packages = site.getsitepackages()
    for path in site_packages:
        print(f"Lisensi untuk paket di {path}.")

list_licenses()
# Fungsi: Mendaftar di mana paket berada untuk mengaudit lisensi.
# Kondisi: Ketika Anda ingin memeriksa kepatuhan terhadap lisensi di paket pihak ketiga.