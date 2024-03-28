gaji = int(input("'masukkan gaji Pegawai: "))

status1 = input("Apakah sudah berkeluarga? (Ya/Tidak) : ")
status1.capitalize()
if status1 == "Ya":
  berkeluarga = True
elif status1 == "Tidak":
  berkeluarga = False
else:
  pass

status2 = input("Apakah sudah memiliki rumah? (Ya/Tidak) : ")
status2.capitalize()
if status2 == "Ya":
  punya_rumah = True
elif status2 == "Tidak":
  punya_rumah = False
else:
  pass


if gaji > 4000000:
    print ("Gaji sudah diatas UMR")
    if berkeluarga:
        print ("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print ("Tidak perlu ikutan asuransi")

    if punya_rumah:
        print ("wajib bayar pajak rumah")
    else:
        print ("tidak wajib bayar pajak rumah")
else:
    print ("Gaji belum UMR")
