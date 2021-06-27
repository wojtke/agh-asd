"""
Quicksort - sorts quite quickly

expected O(nlogn), worst case O(n^2)

"""

def partition(T, p, q):
    # Lomuto
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

def partition_hoare(T, p, q):
    pivot = T[ (p+q)//2 ]
    while True:
        while T[p] < pivot:
            p += 1

        while T[q] > pivot:
            q -= 1

        if p >= q:
            return q

        T[p], T[q] = T[q], T[p]
        p+=1
        q-=1


# normal recursive function - lomuto
def rec_qs(T, p, q):
    #[p, q]
    if p < q:
        pivot = partition_hoare(T, p, q)
        rec_qs(T, p, pivot-1)
        rec_qs(T, pivot+1, q)

# recursive function - hoare
# in hoare's partition we don't know where pivot ends up,
# probably not in the middle like in lomuto's partition
def rec_qs_hoare(T, p, q): 
    #[p, q]
    if p < q:
        pivot = partition_hoare(T, p, q)
        rec_qs(T, p, pivot)
        rec_qs(T, pivot+1, q)

# recursive function that greatly reduces worst case stack memory usage
# reduces worst case memory usage from O(n) to O(logn)
def rec_qs_reduced_stack(T, p, q):
    #[p, q]
    while p < q:
        pivot = partition(T, p, q)
        rec_qs_reduced_stack(T, p, pivot-1)
        p = pivot+1


# example

from random import randint
T = [randint(0,50) for _ in range(10)]
print(T)
rec_qs(T, 0, len(T)-1)
print(T)