def insert(T, n, val):
    T[n]=val
    parent = (n-1)//2

    while T[parent]<val:
        T[parent], T[n] = T[n], T[parent]
        n = parent
        parent = (n-1)//2

 
def heapify(T, n, i):
    largest = i  
    l = 2 * i + 1    
    r = 2 * i + 2 
 
    if l < n and T[largest] < T[l]:
        largest = l
 
    if r < n and T[largest] < T[r]:
        largest = r
 
    if largest != i:
        T[i], T[largest] = T[largest], T[i] 
        heapify(T, n, largest)
 
def heapSort(T):
    n = len(T)
 
    for i in range(n//2 - 1, -1, -1):
        heapify(T, n, i)
 
    for i in range(n-1, 0, -1):
        T[i], T[0] = T[0], T[i]  
        heapify(T, i, 0)
 
 