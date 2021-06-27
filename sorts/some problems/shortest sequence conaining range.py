"""
Shortest subsequence containing all elements from range (0 - n-1).

Works in linear time.
"""

def ss(T, n):
	count_t = [0]*n
	zeros = n

	i=0
	while zeros > 0 and i<len(T):
		if count_t[ T[i] ] == 0:
			zeros-=1
		count_t[ T[i] ] += 1
		i+=1

	if zeros > 0:
		return None

	shortest = i

	a, b = 0, i
	while b<len(T):
		if zeros == 0:
			shortest = min(shortest, b-a)

			count_t[ T[a] ]-=1
			if count_t[ T[a] ] == 0:
				zeros+=1
			a+=1
		elif zeros > 0:
			if count_t[ T[i] ] == 0:
				zeros-=1
			count_t[ T[i] ] += 1
			b+=1

	return shortest


# example
from random import randint
T = [randint(0,3) for _ in range(25)]
print(T)
print(ss(T, 4))