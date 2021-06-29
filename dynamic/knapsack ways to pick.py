"""
Like knapsack, but the problem is to identify how many ways are there to pick items 
with minimum profit and max weight.

F[i][p][w] - how many ways to pick from first i items, with total profit>=p and total weight<=w

"""

def f(F, i, p, w):
	if w<0 or i<0:
		return 0

	if p <= 0 and i==0:
		return 1

	if F[i][p][w] is not None:
		return F[i][p][w]

	F[i][p][w] = f(F, i-1, p-P[i-1], w-W[i-1]) + f(F, i-1, p, w)

	return F[i][p][w]

def knapsack_ways_to_pick(P, W, min_profit, max_weight):
	n = len(P)
	F = [[[None]*(max_weight+1) for _ in range(sum(P)+1)] for _ in range(n+1)]
	return f(F, n, min_profit, max_weight)


# example

P = [2,6,8,2,7]
W = [6,3,7,9,3]

print(knapsack_ways_to_pick(P, W, 10, 15))
