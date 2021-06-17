

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

def knapsack2(P, W, max_weight):
	n = len(W)

	#F[i][w] - max profit z i pierwszych przedmiotow nie przekraczajac w wagi
	F = [[0]*(max_weight+1) for _ in range(n+1)]

	for i in range(1,n+1):

		for w in range(1, max_weight+1):

			if w>=W[i-1]:
				F[i][w] = max(F[i-1][w], F[i-1][w-W[i-1]] + P[i-1])
			else:
				F[i][w] = F[i-1][w]

	return F[n][max_weight]

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


P = [2,6,8,2,7]
W = [6,3,7,9,3]

print(knapsack2(P, W, 15))