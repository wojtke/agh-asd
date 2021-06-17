def selection_sort(T):
    for i in range(len(T)): 
          
        min_idx = i 
        for j in range(i+1, len(T)): 
            if T[min_idx] > T[j]: 
                min_idx = j 
                  
        T[i], T[min_idx] = T[min_idx], T[i] 

def insertion_sort(T): 
    for i in range(1, len(T)): 
  
        key = T[i] 
  
        j = i-1
        while j >=0 and key < T[j]: 
            T[j+1] = T[j] 
            j -= 1
        T[j+1] = key

def selection_sort_partial(T, p, q):
    #[p, q)
    for i in range(p, q): 
          
        min_idx = i 
        for j in range(i+1, q): 
            if T[min_idx] > T[j]: 
                min_idx = j 
                  
        T[i], T[min_idx] = T[min_idx], T[i] 

def insertion_sort_partial(T, p, q): 
    #[p, q)
    for i in range(p+1, q): 
  
        key = T[i] 
  
        j = i-1
        while j >= p and key < T[j]: 
            T[j+1] = T[j] 
            j -= 1
        T[j+1] = key
        