"""
Problem: 
A frog jumps on the x-axis. It needs to get from 0 to n-1 jumping only towards
greater numbers. Each jump consumes energy equal to the distance of a jump. On some numbers,
there are snack that the frog can consume to get energy. 

A[i] - energy from eating the snack on number i
Find the minimum number of jumps required to get from 0 to n-1

Solution:
F[i][j] - min number of jumps to get to number i with j energy

"""

def frog(A):
	max_energy = sum(A)
	n = len(A)

	F = [[None]*(max_energy+1) for _ in range(n)]

	F[0][0] = 0

	def f(i, j):
		j = max(0, j)

		if F[i][j] != None:
			return F[i][j]

		best = None
		k=1
		while k<=i and f(i-k, j+k-A[i-k]) != None:
			case =  1 + f(i-k, j+k-A[i-k])
			if best == None or best>case:
				best = case
			k+=1
		F[i][j] = best

		return F[i][j]

	return f(n-1, 0)


# example

A = [2,1,1,0,3,2,0,0,5,1,0,2,0,1,0,1,0,1]
print(frog(A))