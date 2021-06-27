"""
Radixsort/counting sort
sorts nonnegative integer values in linear time

To use as normal counting sort, use base = max(T)
"""

def countingSort(T, base, exp=0): 
    n = len(T) 
  
    output = [0] * n
    count = [0] * base
    
    # counting
    div = base**exp
    for x in T: 
        index = (x // div) % base
        count[index] += 1
    
    # prefix sum
    for i in range(1, base): 
        count[i] += count[i - 1] 

    # rearranging
    i = n - 1
    while i >= 0: 
        index = (T[i] // div) % base
        output[count[index] - 1] = T[i] 
        count[index] -= 1
        i -= 1

    # copying the array
    for i in range(n):
        T[i]=output[i]


def radixSort(T, base): 
    biggest = max(T) 
   
    i=0
    while biggest // base**i > 0: 
        countingSort(T, base, i) 
        i+=1

    return T


# example

from random import randint

T = [randint(0, 255) for _ in range(16)]
print(T)
radixSort(T, 16)
print(T)