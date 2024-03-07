a=100
b=12.5
c=a+b
d="Najmi"
e= 1+2j
f = ["najmi", 12, "lallaalala", 23, 13] #list
g = ("najmi", "haha", "mimi", 1, 2, 8, 1000) #tuple
h = {"ami", "ami", 1, 2, 3, 2, 5} # tipe data set
i = {1:"najmiiwiwiwi", 2:"wawa cat", 'miaw':2, 8:1000} #tipe data dictionary elemen tidak memiliki indeks akan tetapi dapat dipanggil menggunakan key. Struktur dict adalah key:value
print(type(a)) 
print(type(b))
print(type(c))
print(type(d))
print(type(e)) #tipe data complex
print(type(f)) # tipe data list anggotanya lebih dinamis dapat diubah sewaktu waktu
print(type(g)) # tipe data tuple isi dari datanya tidak dapat diubah
print(type(h)) # tipe data set unordered (tidak berurut)  Kita juga bisa membuat set dari list dengan memasukkan list ke dalam fungsi set()
print(type(i)) # tipe data dictionary elemen tidak memiliki indeks akan tetapi dapat dipanggil menggunakan key. Struktur dict adalah key:value
print(d[0:5])
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])
print(f[0:3])
print(h)