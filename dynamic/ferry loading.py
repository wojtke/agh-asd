"""
Problem:
Ferry with two lanes of length L is being loaded with cars of length A[i]. 
How many cars can we fit, if we are not allowed to skip them 
and change the order in which they get loaded, only choose left or right lane?

Solution:
F[i][a] - can we fit first i cars with first lane filled to length a
"""


def ferry(A, L):
	n = len(A)
	Asums = [sum(A[:i]) for i in range(len(A))]

	F = [[None]*(L+1) for _ in range(n+1)]

	F[0][L] = True

	def f(i, a):
		b = 2*L - a - Asums[i]

		if a>L or b>L:
			return False

		if F[i][a] is not None:
			return F[i][a]

		F[i][a] =  f(i-1, a+A[i-1]) or f(i-1, a)

		return F[i][a]


	i=n
	while sum(A[:i])>2*L:
		i-=1

	while i>=0:
		for a in range(L+1):
			if f(i, a):
				return i
		i-=1

	return i

# example

from random import randint, seed

seed(1337)
A = [randint(10,50) for _ in range(10)]
L = sum(A)//4

print(A, L)
print(ferry(A, L))