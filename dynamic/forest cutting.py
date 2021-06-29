"""
Problem:
Maximalize profit from cutting trees, but cannot cut two trees in a row. Profit from tree i: A[i].

Solution:
 f(i) - max profit from cuttin trees up to i
 f(i) = max(A[i] + f(i-2), f(i-1))

"""

def forest(A):
	F = [0]*len(A)
	P = [0]*len(A)

	F[0]=A[0]
	F[1]=max(A[0], A[1])

	P[0]=2
	if A[0]>A[1]:
		P[1] = 1
	else:
		P[1] = 2

	for i in range(2, len(A)):
		F[i] = max(A[i] + F[i-2], F[i-1])
		if A[i] + F[i-2]>F[i-1]:
			P[i] = 2
		else:
			P[i] = 1


	# which trees to cut
	trees = []
	i = len(A)-1
	while i>=0:
		if P[i]==2:
			trees+=[i]
			i-=2
		else:
			i-=1

	print(trees)

	return F[len(A)-1] 

# example

A = [9,5,2,6,6,8,4,8,4,7,6,4]

print(forest(A))