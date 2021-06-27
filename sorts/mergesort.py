"""
Mergesort - O(nlogn) time, O(n) memory

"""

def mergesort(T):
  def ms(T, t, p, q):
    # [p,q)
    if q-p==1:
      return
      
    split = (p+q+1)//2
    ms(T, t, p, split)
    ms(T, t, split, q)

    i, j = 0, 0
    while p+i<split and split+j<q:
      if T[p+i]<T[split+j]:
        t[p+i+j]=T[p+i]
        i+=1
      else:
        t[p+i+j]=T[split+j]
        j+=1

    while p+i<split:
      t[p+i+j]=T[p+i]
      i+=1
    while split+j<q:
      t[p+i+j]=T[split+j]
      j+=1

    while p<q:
      T[p]=t[p]
      p+=1

    return

  # t - auxiliary array
  t = [None]*len(T)

  ms(T, t, 0, len(T))

# cool way to count inversions in an array using mergesort

def mergesort_inversions(T):
  def ms(T, t, p, q):
    if q-p==1:
      return 0
    
    inv = 0
    split = (p+q+1)//2
    inv+=ms(T, t, p, split)
    inv+=ms(T, t, split, q)

    i, j = 0, 0
    while p+i<split and split+j<q:
      if T[p+i]<T[split+j]:
        t[p+i+j]=T[p+i]
        i+=1
      else:
        t[p+i+j]=T[split+j]
        j+=1
        inv+=1

    while p+i<split:
      t[p+i+j]=T[p+i]
      i+=1
    while split+j<q:
      t[p+i+j]=T[split+j]
      j+=1

    while p<q:
      T[p]=t[p]
      p+=1

    return inv

  # t - auxiliary array
  t = [None]*len(T)

  return ms(T, t, 0, len(T))

# example 

T = [1,3,2,55,51,12,34,6,3]
print(T)
print("inversions: ", mergesort_inversions(T[:]))
mergesort(T)
print(T)

