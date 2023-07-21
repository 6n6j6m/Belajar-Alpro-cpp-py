#Konversi Waktu ke  satuan Detik
def waktu_ke_detik(jam, menit, detik):
    total_detik = jam * 3600 + menit * 60 + detik
    return total_detik

#Konversi Satuan Detik ke Waktu(jam, menit, detik)  
def detik_ke_waktu(total_detik):
    jam = total_detik // 3600
    sisa_detik = total_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return jam, menit, detik

#input waktu
jaminput = int(input("Masukkan jumlah jam: "))
menitinput = int(input("Masukkan jumlah menit: "))
detikinput = int(input("Masukkan jumlah detik: "))

total_detik = waktu_ke_detik(jaminput, menitinput, detikinput)
print("Total detik:", total_detik, "detik.")

# fungsi untuk mengembalikan ke waktu
total_detik_input = int(input("Masukkan total detik: "))

jam_hasil, menit_hasil, detik_hasil = detik_ke_waktu(total_detik_input)
print(f"Waktu: {jam_hasil} jam, {menit_hasil} menit, {detik_hasil} detik.")
