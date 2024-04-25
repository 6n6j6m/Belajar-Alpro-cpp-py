# Buatlah program untuk menentukan umur seseorang,dengan inputan tahun sekarang dan tahun lahir, kemudian buat kondisi untuk menentukan kategori usianya, dengan kriteria sebagai berikut :

# Jika umur 0 – 4 tahun maka kategori usianya adalah Balita
# Jika umur 5 – 11 tahun maka kategori usianya adalah Kanak-kanak
# Jika umur 12 – 25 tahun maka kategori usianya adalah Remaja
# Jika umur 26 – 45 tahun maka kategori usianya adalah Dewasa
# Jika umur 46 – 65 tahun maka kategori usianya adalah Lansia
# Jika umur 66 – diatasnya tahun maka kategori usianya adalah Manula

# Program KLASIFIKASI UMUR

tahun_sekarang = int(input("Tahun Sekarang : "))
tahun_lahir = int(input("Tahun Lahir : "))
umur = tahun_sekarang - tahun_lahir

if (umur <= 4):
    kategori = "Balita"
elif (umur <= 11):
    kategori = "Kanak-kanak"
elif (umur <= 25):
    kategori = "Remaja"
elif (umur <= 45):
    kategori = "Dewasa"
elif (umur <= 65):
    kategori = "Lansia"
else:
    kategori = "Manula"

print("Umur anda adalah ", umur)
print("Kategori anda adalah ", kategori)