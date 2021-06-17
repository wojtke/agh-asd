from math import log2
G = [[1, 1, 1, 1],
	[1, 1, 1, 0.9],
	[1, 1, 1, 1],
	[1, 1, 1, 1]]



def arbitraz(G):
	n = len(G)

	for i in range(n):
		for j in range(n):
			G[i][j] = log2(G[i][j])

	for t in range(n):
		for u in range(n):
			for v in range(n):
				G[u][v] = min(G[u][v], G[u][t] - G[t][v])

				if u==v and G[u][v]<0:
					return True

	return False

print(arbitraz(G))