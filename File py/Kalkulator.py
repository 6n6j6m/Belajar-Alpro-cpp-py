def hitung(a, b, pilih):
    match pilih:
        case 1:
            hasil = a + b
            return hasil
        case 2:
            hasil = a - b
            return hasil
        case 3:
            hasil = a * b
            return hasil
        case 4:
            hasil = a/b
            return hasil        

print("Program Kalkulator Sederhana")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi\n")

a = float(input("Masukkan bilangan pertama : "))
b = float(input("Masukkan bilangan kedua : "))

pilih = int(input("Pilih Operasi aritmatika yang akan digunakan : "))

print("Hasilnya adalah : ", hitung(a, b, pilih))
