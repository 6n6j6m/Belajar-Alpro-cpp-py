print("Program Konversi Celcius ke Suhu berbeda")
print("1.Celcius ke Reamur")
print("2.Celcius ke Fahrenheit")
print("3.Celcius ke Kelvin")
print("4.Celcius ke Rankine")

pilih = int(input("Pilih jenis konversi(1,2,3 atau 4) : "))
suhu = float(input("Masukkan besar suhu dalam celcius : "))

# 1. Rumus konversi suhu Celcius ke Fahrenheit: 
#         ⁰F = (9/5) × ⁰C + 32

# 2. Rumus konversi suhu Celcius ke Kelvin:
#         K= ⁰C + 273,15

# 3. Rumus konversi suhu Celcius ke Reamur:
#         ⁰R = (4/5) ⁰C

# 4. Rumus konversi suhu Celcius ke Rankine:
#         ⁰Ra = (⁰C + 273.15) × 9/5

if pilih == 1:
    hasilkonversi = (4.0/5.0) * suhu
    print(suhu, "Celcius = ", hasilkonversi, " Reamur")
elif pilih == 2:
    hasilkonversi = (9.0/5.0) * suhu + 32
    print(suhu, "Celcius = ", hasilkonversi, " Fahrenheit")
elif pilih == 3:
    hasilkonversi = suhu + 273.15
    print(suhu, "Celcius = ", hasilkonversi, " Kelvin")
elif pilih == 4:
    hasilkonversi = ((suhu + 273.15) * 9.0)/5.0
    print(suhu, "Celcius = ", hasilkonversi, " Rankine")
else:
    print("Tidak ada")