"""
Quickselect - uses partition function, same as in quicksort
to find k'th element (as if the array was sorted)
in an array in expected O(n), but worst case O(n^2) time.
"""

def partition(T, p, q):
    #[p, q]

    # i - last element smaller than pivot
    # j - current element
    pivot  = T[q]
    i=p-1
    for j in range(p,q):
        if T[j]<=pivot:
            i+=1
            T[i], T[j] = T[j], T[i]

    # putting pivot element to the center
    T[i+1], T[q] = T[q], T[i+1]

    # returning the index of pivot element
    return i+1

def quickselect(tab, p, q, k):
	if p==q:
		return tab[p]

	pivot = partition(tab, p, q)

	if k>pivot:
		return quickselect(tab, pivot+1, q, k)
	elif k<pivot:
		return quickselect(tab, p, pivot-1, k)
	else: # pivot==k
		return tab[pivot]



print(quickselect(A, 0, n-1, 5))
print(A)


