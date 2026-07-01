import site
import sys

def add_site_packages():
    site.addsitedir('/another/custom/path')
    print("Custom path ditambahkan ke sys.path.")

add_site_packages()
print("Daftar sys.path setelah penambahan:")
print(sys.path)
# Fungsi: Memanipulasi jalur dan menambahkan direktori kustom.
# Kondisi: Ketika Anda ingin mengelola modular path secara dinamis.