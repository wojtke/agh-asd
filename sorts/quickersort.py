"""
Quicker sort - like quicksort, but partitions elements to those:
    smaller than pivot
    equal to pivot
    greater than pivot
meaning it will work faster than quicksort on arrays with redundant values.
"""

def partition_3way(T, lo, hi):
    # [lo, hi)
    pivot = T[lo] # any pivot will do

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


def rec_quicker_sort(T, p, q):
    #[p, q)
    if p < q:
        left, right = partition_3way(T, p, q)
        rec_quicker_sort(T, p, left)
        rec_quicker_sort(T, right, q)

# example

T = [0, 1, 123, 12, 12, 12, 12, 0, 12, 13]
print(T)
rec_quicker_sort(T, 0, len(T))
print(T)