
def countingSort(T, base, exp): 
    n = len(T) 
  
    output = [0] * n
    count = [0] * base
    
    # zliczanie
    div = base**exp
    for x in T: 
        index = (x // div) % base
        count[index] += 1
    
    # sumy prefiksowe
    for i in range(1, base): 
        count[i] += count[i - 1] 

    # układanie
    i = n - 1
    while i >= 0: 
        index = (T[i] // div) % base
        output[count[index] - 1] = T[i] 
        count[index] -= 1
        i -= 1

    # kopiowanie tablicy
    for i in range(n):
        T[i]=output[i]



def radixSort(T, base): 
    najwiekszy = max(T) 
   
    i=0
    while najwiekszy // base**i > 0: 
        countingSort(T, base, i) 
        i+=1

    return T


  
from random import randint

T = [randint(0, 255) for _ in range(16)]
print(T)
radixSort(T, 16)
print(T)