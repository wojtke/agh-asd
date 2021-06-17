def floyd_warshall(G):
	n = len(G)

	D = [[G[i][j] if i==j or G[i][j]>0 else float('inf') for j in range(n) ] for i in range(n)]

	N = [[j if G[i][j]>0 or i==j else None for j in range(n)] for i in range(n)]

	for t in range(n):
		for u in range(n):
			for v in range(n):
				if D[u][t] + D[t][v] < D[u][v]:
					D[u][v] = D[u][t] + D[t][v]
					N[u][v] = N[u][t]

	return D, N

def print_path(N, a, b):
	while a!=b:
		print(a, end=" -> ")
		a = N[a][b]
	print(b)

G = [[0, 2, 1, 0, 0, 0, 33],
	[0, 0, 0, 0, 5, 0, 5],
	[0, 0, 0, 0, 0, 0, 2],
	[0, 0, 0, 0, 0, 0, 111],
	[0, 0, 0, 1, 0, 55, 1],
	[141, 0, 0, 0, 0, 0, 0],
	[0, 0, 12, 0, 0, 0, 0]]


D, N = floyd_warshall(G)

print_path(N, 4, 1)




