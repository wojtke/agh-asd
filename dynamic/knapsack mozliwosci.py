def f(F, i, p, w):
	# na ile sposobow mozemy wybrac rzeczy sposrod i pierwszych
	# tak zeby profit z nich byl przynajmniej p, a zajely nie wiecej niz w
	if w<0 or i<0:
		return 0

	if p <= 0 and i==0:
		return 1

	if F[i][p][w] is not None:
		return F[i][p][w]

	F[i][p][w] = f(F, i-1, p-P[i-1], w-W[i-1]) + f(F, i-1, p, w)

	return F[i][p][w]

P = [2,6,8,2,7]
W = [6,3,7,9,3]

def knapsack_ile_mozliwosci(P, W, min_profit, max_weight):
	n = len(P)
	F = [[[None]*(max_weight+1) for _ in range(sum(P)+1)] for _ in range(n+1)]
	return f(F, n, min_profit, max_weight)

print(knapsack_ile_mozliwosci(P, W, 10, 15))
