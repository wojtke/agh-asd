from random import randint
import numpy as np 


n=5
a = np.arange(n**2).reshape((n,n))
a = a - np.arange(n)*n
b = (a- n//2)//n
a += n*(n-1)//2 

print(a)
print(b)