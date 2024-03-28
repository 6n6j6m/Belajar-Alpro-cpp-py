import numpy as np

#membuat matriks segitiga 
tes = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# for x in range(tes):
# 	y = x+1
# 	for y  in range(tes+1):
# 		tes [y, x] -= tes [y, x]
for x in range(len(tes)):
    print(x)
    for y in range(x+1, len(tes)): #dari indeks x+1 sampai len(tes)
	    tes[y, x] -= tes[y, x] 

print(tes) 
