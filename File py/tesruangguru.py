penduduk = 1
int(penduduk)
day = 50

for i in range(2, day + 1):
    if i%3==0:
        penduduk = int(penduduk/2)
    else:
        penduduk *=3

print(penduduk)