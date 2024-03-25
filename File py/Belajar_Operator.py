A = 1
#Replace Value
#operator += yaitu A += 2 maksudnya A = A + 2
A += 2 #maksudnya A = 1 + 2
print(A)

#Operator -= yaitu A -= 2 maksudnya A = A - 2 (Nilai A sekarang 3)
A -= 2 #maksudnya A = 3 - 2
print(A)

#Operator -= yaitu A -= 2 maksudnya A = A - 2 (Nilai A sekarang 1)
A *= 2 #maksudnya A = 1 * 2
print(A)

#Operator -= yaitu A -= 2 maksudnya A = A - 2 (Nilai A sekarang 2)
A /= 0.5 #maksudnya A = 2/0.5
print(A)

#Operator -= yaitu A -= 2 maksudnya A = A - 2 (Nilai A sekarang 4)
A%=3 #maksudnya A = 4%3
print(A)

#Logical operator
x = True
y = False
z = x and y
print(z) 

klm = "saya suka makan gado-gado dan nasi goreng"
print(klm[0:16])
print(klm[0:9], klm[16:26])
print(klm[0:15], klm[30:41], klm[26:29], klm[16:26])
print(klm[-4])
print(klm[-9:-1]) #indeks negatif dimulai dari huruf paling kanan / karakter terakhir / elemen terakhir 

kalimat = input("Masukkan kalimat : ")
m = int(input("mulai dari indeks ke : "))
n = int(input("berakhir di indeks : "))
print(kalimat[m:n])
