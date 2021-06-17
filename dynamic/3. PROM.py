def knapsack(P, W, max_weight):
	n = len(W)

	F = [[0]*(max_weight+1) for _ in range(n)]

	for w in range(W[0], max_weight+1):
		F[0][w] = P[0]

	for i in range(1,n):

		for w in range(1, max_weight+1):

			if w>=W[i]:
				F[i][w] = max(F[i-1][w], F[i-1][w-W[i]] + P[i])
			else:
				F[i][w] = F[i-1][w]

	return F[n-1][max_weight], F
	
def ferry(A, L):
	n = len(A)

	i = n
	while sum(A[:i])>2*L:
		i-=1
	while i>0:	
		pas1, F = knapsack(A[:i], A[:i], L)
		pas2 = sum(A[:i]) - pas1


		if pas2 <= L:

			pas1_index = getKnapsackSolution(F, A[:i], A[:i], i-1, pas1)
			pas2_index = [x for x in range(i) if x not in pas1_index]


			print(pas1_index, sum([A[i] for i in pas1_index]))
			print(pas2_index, sum([A[i] for i in pas2_index]))

			return i

		i-=1

from random import randint, seed

seed(1337)
A = [randint(10,50) for _ in range(10)]
L = sum(A)//4

print(A, L)


def getKnapsackSolution(F, W, P, i, w):
	if i<0:
		return []
	if i==0:
		if w>=W[0]:
			return [0]
		else:
			return []

	if w>=W[i] and F[i][w] == F[i-1][w-W[i]] + P[i]:
		return getKnapsackSolution(F, W, P, i-1, w-W[i]) + [i]
	else:
		return getKnapsackSolution(F, W, P, i-1, w)


print(ferry(A, L))
