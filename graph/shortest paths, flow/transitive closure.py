G = [[0, 1, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 0, 0],
	[0, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 1, 1],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0]]

def domkniecie_przechodnie(G):
	n = len(G)
	for t in range(n):
		for u in range(n):
			for v in range(n):
				G[u][v] = G[u][v] or (G[u][t] and G[t][v])
	return G


g = domkniecie_przechodnie(G)

for row in g:
	print(row)

