from random import randint, shuffle, seed

def mediana(A, p, q):
  """Selection sort od p do q,
  zwraca indeks mediany"""
  for i in range(p, q): 

    min_idx = i 
    for j in range(i+1, q): 
      if A[min_idx] > A[j]: 
        min_idx = j 
      
    A[i], A[min_idx] = A[min_idx], A[i] 

  return (p+q)//2

def partition(T, p, q):
    """Partition taki, że pivot jest pierwszym elementem,
    tj o indeksie p"""

    pivot = T[p]
    i=p

    for j in range(p+1,q+1):
        if T[j]<=pivot:
            i+=1
            T[i], T[j] = T[j], T[i]

    T[i], T[p] = T[p], T[i]

    return i


def linearselect( A, k, first=0, last=None):
  """
  Pracuje na tablicy A, na przedziale indeksów od first do last,
  (włącznie z last - przedział obustronnie zamknięty)
  Funckja nie tworzy żadnej nowej tablicy, pracuje w miejscu.
  """

  last = last or len(A)-1

  if first==last:
    return A[first]

  # pełne piątki, wyciągam ich mediany na początek tj. od indeksu first
  i=0
  while i<(last+1-first)//5:
    m = mediana(A, first+5*i, first+5*i+4)
    A[first+i], A[m] = A[m], A[first+i]
    i+=1

  # ostatnia, niepełna piątka
  if (last+1-first)%5!=0:
    m = mediana(A, first+5*i, last) 
    A[first+i], A[m] = A[m], A[first+i]
    i+=1

  '''
   Sprawdzamy czy mamy jedną medianę - jeśli nie, to liczymy medianę median rekurencyjnie.
   Będzie ona zawsze wrzucona na indeks first w tablicy,
   dlatego nigdzie explicite nie podaję pivota, partition bierze
   go z początku przedziału na jakim jest wywoływany
  '''
  if i > 1:
    linearselect(A, first+i//2, first=first, last=(first+i-1))

  pivot = partition(A, first, last)

  if pivot==k:
    return A[pivot]
  if k>pivot:
    return linearselect(A, k, first=pivot+1, last=last)
  else:
    return linearselect(A, k, first=first, last=pivot-1)




seed(42)

n = 100
for i in range(n):
  A = list(range(4000))
  shuffle(A)
  x = linearselect( A, i )
  if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)
    
print("OK")

