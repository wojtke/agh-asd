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
         
    # do kubełków
    for x in T:
        buckets[int(k*x/m)].append(x)
     
    # sortowanie w kubełkach 
    for i in range(k):
        buckets[i] = insertion_sort(buckets[i])
    
    # wybieranie z kubełków  
    i=0
    for bucket in buckets:
        for x in bucket:
            T[i]=x
            i+=1

    return T
 
# Driver Code
T = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434] 
print(T)
T = bucketSort(T, 6)
print(T)
 
# This code is contributed by
# Oneil Hsiao