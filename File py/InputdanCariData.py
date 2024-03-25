N = int(input("Input N: "))
mahasiswa = []
nmax = -1 #Data sentinel
nmin = 5.0 #Data sentinel
nlulus = 0 

for i in range(N):
    print("Data Mahasiswa ke-", i+1)
    nama = input("Nama: ")
    nim = input("NIM: ")
    IPK = float(input("IPK: "))

    mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "IPK": IPK
    })

    if IPK >= 2.0:
        nlulus += 1

    if IPK > nmax:
        nmax = IPK

    if IPK < nmin:
        nmin = IPK

print("Nilai maksimum: ", nmax)
print("Nilai minimum: ", nmin)
print("Banyak nilai lulus: ", nlulus)
print("Nilai yang lulus: ", end="")
for mhs in mahasiswa:
    if mhs["IPK"] >= 2.0:
        print(mhs["IPK"], end=" ")

cari = input("\nCari nim: ")
hasilcari = False
for mhs in mahasiswa:
    if mhs["nim"] == cari:
        print("Nama: ", mhs["nama"])
        print("IPK: ", mhs["IPK"])
        hasilcari = True
        break

if not hasilcari:
    print("mhs tsb tak ditemukan")
