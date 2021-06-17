G = [ 
	[1, 2, 3],
	[0, 2],
	[0, 1, 3],
	[0, 2],
	]


def cykl4(G):
	n = len(G)
	T = [[False]*n for _ in range(n)]

	for v in range(n):
		nn = len(G[v])
		for a in range(nn):
			for b in range(a+1, nn):
				va = G[v][a]
				vb = G[v][b]
				if T[va][vb]:
					return True, T
				else:
					T[va][vb] = True

	return False, T

a, t = cykl4(G)
print(a)
for row in t:
	print(row)