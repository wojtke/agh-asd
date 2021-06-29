"""
Problem:
We have a chessboard with fields numbered 0 to n-1. Each field has a value
that we need to pay upon moving onto it.
We need to walk from 0,0 to n-1,n-1 only going right of down. 
What's the minimal cost?

Solution:

F[i][j] - cheapest path from i, j to the end
F[i][j] = min(  F[i][j+1], F[i+1][j] ) + A[i][j]

 i=n-1
 F[i][j] = F[i][j+1] + A[i][j]

 j=n-1
 F[i][j] = F[i][j+1] + A[i][j]

 i=n-1 i j=n-1
 F[i][j] = A[i][j]

"""

def walk(A):
	F = [[0]*n for _ in range(n)]

	F[n-1][n-1] = A[n-1][n-1]

	for i in range(1, n):
		F[n-1][n-1-i] = F[n-1][n-i] + A[n-1][n-1-i]

	for i in range(1, n):
		F[n-1-i][n-1] = F[n-i][n-1] + A[n-1-i][n-1]

	for i in range(n-2, -1, -1):
		for j in range(n-2, -1, -1):
			F[i][j] = min( F[i][j+1], F[i+1][j] ) + A[i][j]

	return F[0][0]


def walk_path(A):
	# prints path
	F = [[0]*n for _ in range(n)]
	P = [[0]*n for _ in range(n)]

	F[n-1][n-1] = A[n-1][n-1]
	P[n-1][n-1] = "end"

	for i in range(1, n):
		F[n-1][n-1-i] = F[n-1][n-i] + A[n-1][n-1-i]
		P[n-1][n-1-i] = "right"

	for i in range(1, n):
		F[n-1-i][n-1] = F[n-i][n-1] + A[n-1-i][n-1]
		P[n-1-i][n-1] = "down"

	for i in range(n-2, -1, -1):
		for j in range(n-2, -1, -1):
			if F[i][j+1]>F[i+1][j]:
				F[i][j] = F[i+1][j] + A[i][j]
				P[i][j] = "down"
			else:
				F[i][j] =F[i][j+1] + A[i][j]
				P[i][j] = "right"

	
	i, j = 0, 0
	print("Start:", i, j)
	while P[i][j] != "end":
		print(P[i][j], end=" ")
		if P[i][j] == "down":
			i+=1
		elif P[i][j] == "right":
			j+=1
		print( i, j, f"(val {A[i][j]})")
	print("End")

	return F[0][0]

# example 

from random import random, randint
n=5
A = [[randint(1,5) for _ in range(n)] for _ in range(n)]

for row in A:
	print(row)
print(walk_path(A))
