V = [12,25,10,5]
H = [5, 12, 5, 3]
W = [5, 2, 10, 5]


# f(i, h, w) - najwiekszy koszt sposrod i pierwszych przedmiotow, 
# 				nie przekraczajac h wysokosci oraz w wagi

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


a = knapsack2d(V, H, W, 15, 10)

print(a)