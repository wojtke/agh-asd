def mergesort(T, p, q, Tpomoc=None):
	Tpomoc=Tpomoc or [None]*len(T)

	if q-p<2:
		return

	split = (p+q+1)//2
	
	mergesort(T, p, split, Tpomoc)
	mergesort(T, split, q, Tpomoc)

	i=0
	j=0

	while p+i<split and split+j<q:
		if T[p+i]<T[split+j]:
			Tpomoc[p+i+j]=T[p+i]
			i+=1
		else:
			Tpomoc[p+i+j]=T[split+j]
			j+=1

	while p+i<split:
		Tpomoc[p+i+j]=T[p+i]
		i+=1
	while split+j<q:
		Tpomoc[p+i+j]=T[split+j]
		j+=1

	while p<q:
		T[p]=Tpomoc[p]
		p+=1


'''
T = [24,51,4,5,1,5,4,57,7,73,23,45,1]
print(T)
mergesort(T, 0, len(T))
print(T)
'''

def mergesort_inversions(T, p, q, Tpomoc=None):
	Tpomoc=Tpomoc or [None]*len(T)

	if q-p<2:
		return 0

	split = (p+q+1)//2
	
	inv=0

	inv+=mergesort_inversions(T, p, split, Tpomoc)
	inv+=mergesort_inversions(T, split, q, Tpomoc)

	i=0
	j=0

	while p+i<split and split+j<q:
		if T[p+i]<T[split+j]:
			Tpomoc[p+i+j]=T[p+i]
			i+=1
		else:
			Tpomoc[p+i+j]=T[split+j]
			j+=1
			inv+=1

	while p+i<split:
		Tpomoc[p+i+j]=T[p+i]
		i+=1

	while split+j<q:
		Tpomoc[p+i+j]=T[split+j]
		j+=1

	while p<q:
		T[p]=Tpomoc[p]
		p+=1

	return inv


'''
T = [1,3,2,5]
print(T)
print(mergesort_inversions(T, 0, len(T)))
print(T)
'''