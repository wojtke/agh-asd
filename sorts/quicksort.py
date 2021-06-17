
def partition(T, p, q):
    #[p, q]
    pivot  = T[q]
    i=p-1
    for j in range(p,q):
        if T[j]<=pivot:
            i+=1
            T[i], T[j] = T[j], T[i]

    T[i+1], T[q] = T[q], T[i+1]

    return i+1

def partition_3way(T, lo, hi):
    #[lo, hi)
    pivot = T[lo] #dowolny

    mid = lo
    while mid < hi: 
        if T[mid] < pivot: 
            T[lo], T[mid] = T[mid], T[lo] 
            lo += 1
            mid += 1
        elif T[mid] == pivot: 
            mid += 1
        else: 
            hi -= 1
            T[mid], T[hi] = T[hi], T[mid]  
            

    return lo, hi 

def rec_qs(T, p, q):
    #[p, q]
    if p < q:
        pivot = partition(T, p, q)
        rec_qs(T, p, pivot-1)
        rec_qs(T, pivot+1, q)

def rec_qs_reduced_stack(T, p, q):
    #[p, q]
    while p < q:
        pivot = partition(T, p, q)
        rec_qs_reduced_stack(T, p, pivot-1)
        p = pivot+1

def rec_quicker_sort(T, p, q):
    #[p, q)
    if p < q:
        left, right = partition_3way(T, p, q)
        rec_quicker_sort(T, p, left)
        rec_quicker_sort(T, right, q)


from random import randint
T = [randint(0,2) for _ in range(10)]
print(T)
rec_quicker_sort(T, 0, len(T))
print(T)