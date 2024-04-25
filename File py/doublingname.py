nama = input("Masukkan nama : ")

if " " not in nama or len(nama) < 10:
  nama += " " + nama
  print("Nama nya adalah : ", nama)