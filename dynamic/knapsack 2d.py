"""
Knapsack, but additional restrictions.
The goal is to find most profitable subset of items under total weight limitation
and also under total height limitation.

Input:
	P[i] - profit for item i
	W[i] - weight of item i
	H[i] - height of item i
	max_weight - total weight of items that cannot be exceeded
	max_height - total height of items that cannot be exceeded

F[i][h][w] - max profit from first i items with total weight<=w and total height<=h

"""

def knapsack2d(V, H, W, maxH, maxW):
	n = len(V)
	F = [[[0]*(maxW+1) for _ in range(maxH+1)] for _ in range(n+1)]

	for i in range(n+1):
		for h in range(maxH+1):
			for w in range(maxW+1):

				if h-H[i-1]>=0 and w-W[i-1]>=0:
					F[i][h][w] = max(F[i-1][h][w], F[i-1][h-H[i-1]][w-W[i-1]] + V[i-1])
				else:
					F[i][h][w] = F[i-1][h][w]

	return F[n][maxH][maxW]


# example

V = [12,25,10,5]
H = [5, 12, 5, 3]
W = [5, 2, 10, 5]

a = knapsack2d(V, H, W, 15, 10)

print(a)