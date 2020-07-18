import time
i = 1
#Array dibawah adalah array waktu pelanggan
l= [5,10,3,11,2,9,14,77,13,2]
hasil = []
print("")
print("jumlah pelanggan sebanyak ", len(l) , " orang, dengan waktu masing-masing pelayanan adalah ", l)
print("")
l.sort(reverse=False)
print("Setelah di urutkan maka urutan waktu pelanggan akan seperti ini") 
print(l)
print ("\n")
start = time.time()
ix = 0
jum = 0
while ix < len(l) :
	jx = 0
	while jx <= ix :
		jum = jum + l[jx]
		jx = jx + 1
	ix = ix + 1
print(" --> Waktu paling optimal untuk melayani sebanyak ", len(l)," orang adalah ", jum , " detik")
print()
print("Dengan urutan waktu sebagai berikut : ", l)
end = time.time()
print ("Execution time is ")
print(end - start)
	
