import time
from itertools import permutations
from os import system
#Array dibawah adalah array waktu pelanggan
ArrayWaktu = [5,10,3,11,2,9,14,77,13,2]
i = 0
JumWaktu = 0
baru = []
print("")
print("Jumlah pelanggan sebanyak ", len(ArrayWaktu) , " orang, dengan waktu masing-masing pelayanan adalah ", ArrayWaktu)
print("")
start = time.time()
perm = permutations(ArrayWaktu)
print("Sistem sedang melakukan perhitungan ...")
print("")
for j in perm:
	i = 0
	JumWaktu = 0
	while i < len(j):
		k = 0
		while k <= i:
			JumWaktu = JumWaktu + j[k]
			k = k + 1
		i = i + 1 
	baru.append(JumWaktu)
baru.sort() 
ArrayWaktu.sort()
# system('cls')
print(" --> Waktu paling optimal untuk melayani sebanyak ", len(ArrayWaktu)," orang adalah ", baru[0] , " detik")
print()
print("Dengan urutan waktu sebagai berikut : ", ArrayWaktu)
end = time.time()
print("waktu program = ", end-start, "detik")
if(end - start > 120) :
	menit = (end - start) / 60
	print("Waktu dalam menit : ", menit , "menit")
