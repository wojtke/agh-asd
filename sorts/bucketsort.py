"""
Bucket sort

Sorts "real" numbers dividing them into k buckets,
then uses insertion sort inside a bucket.

k should be proportional to length of sorted array

Works well only for uniform distribution of data. 
If not evenly distributed, worst case may be O(n^2).
If evenly distributed, expected runtime is O(n)

"""

def insertion_sort(T): 
    for i in range(1, len(T)): 
        key = T[i] 
        j = i-1
        while j >=0 and key < T[j]: 
            T[j+1] = T[j] 
            j -= 1
        T[j+1] = key
    
    return T 
             
def bucketSort(T, k):
    buckets = [[] for _ in range(k)]

    m = max(T)
         
    # into buckets
    for x in T:
        buckets[int(k*x/m)].append(x)
     
    # sorting inside the buckets
    for i in range(k):
        buckets[i] = insertion_sort(buckets[i])
    
    # picking values from the buckets  
    i=0
    for bucket in buckets:
        for x in bucket:
            T[i]=x
            i+=1

    return T
 
# example
T = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434] 

print(T)
T = bucketSort(T, 6)
print(T)
 