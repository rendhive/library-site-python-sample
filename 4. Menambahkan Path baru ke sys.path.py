import site
import sys

custom_path = '/my/custom/path'
site.addsitedir(custom_path)
print("Path telah ditambahkan:")
print(sys.path)
# Fungsi: Menambahkan jalur baru ke dalam list `sys.path`.
# Kondisi: Ketika Anda ingin meload modul dari custom path.