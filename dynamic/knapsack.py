"""
Knapsack problem - finding subset of items that gives most profit but not exceeding some weight

Input:
	P[i] - profit for item i
	W[i] - weight of item i
	max_weight - total weight of items that cannot be exceeded

F[i][w] - max profit from i first items not exceeding w weight

getSolution uses array F to recover which items are picked.

"""

def knapsack(P, W, max_weight):
	n = len(W)

	# F[i][w] - max profit z from i first items not exceeding w weight
	F = [[0]*(max_weight+1) for _ in range(n+1)]

	for i in range(1,n+1):

		for w in range(1, max_weight+1):

			if w>=W[i-1]:
				F[i][w] = max(F[i-1][w], F[i-1][w-W[i-1]] + P[i-1])
			else:
				F[i][w] = F[i-1][w]

	return F[n][max_weight], F

def getSolution(F, W, P, i, w):
	if i==0:
		return []

	if w>=W[i-1] and F[i][w] == F[i-1][w-W[i-1]] + P[i-1]:
		return getSolution(F, W, P, i-1, w-W[i-1]) + [i-1]
	else:
		return getSolution(F, W, P, i-1, w)

# example

P = [2,6,8,2,7]
W = [6,3,7,9,3]

f, F = knapsack(P, W, 15)
print(f)
print(getSolution(F, W, P, len(P), 15))