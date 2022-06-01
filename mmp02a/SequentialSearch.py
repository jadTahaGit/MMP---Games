def sequentialSearch (q, a):
	for i in range(0,len(a)):
		if a[i]==q:
			return i
	return -1

a = [11, 22, 33, 44, 55, 66]
print("Array a: ", a)
print("Search for 55: ",sequentialSearch(55,a))
print("Search for 23: ",sequentialSearch(23,a))
