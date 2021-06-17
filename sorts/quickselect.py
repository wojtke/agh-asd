from random import randint, shuffle, seed
import numpy as np

n=20
A = list(range(n))
shuffle(A)
print(A)


def partition(T, p, q):
    pivot  = T[q]

    # i - ostatni element mniejszy od pivota
    # j - element ukladany aktualnie
    i=p-1

    for j in range(p,q):
        if T[j]<=pivot:
            i+=1
            T[i], T[j] = T[j], T[i]

    # wrzucenie pivota na srodek
    T[i+1], T[q] = T[q], T[i+1]

    # zwraca indeks pivota
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


