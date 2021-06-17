from random import randint
from queue import Queue

n = 8
T = [[randint(1,5) for _ in range(n)] for _ in range(n)]

T = [[5, 5, 1, 2, 5, 4, 1, 1],
	[5, 4, 2, 3, 3, 1, 4, 3],
	[4, 5, 2, 4, 5, 1, 4, 5],
	[5, 3, 4, 3, 3, 4, 1, 5],
	[2, 1, 1, 2, 4, 1, 2, 2],
	[3, 5, 1, 1, 2, 2, 2, 3],
	[2, 1, 2, 3, 4, 4, 1, 4],
	[1, 2, 4, 3, 2, 5, 5, 5]]

for row in T:
	print(row)

def moves(i, j, n):
	moves = [(i+1, j+1),(i-1, j-1),
		(i+1, j),(i-1, j),
		(i, j+1),(i, j-1),
		(i+1, j-1),(i-1, j+1)]

	return [m for m in moves if (0<=m[0]<n and 0<=m[1]<n)]

def dir(a, b):
	arrows = [["🡤", "🡡", "🡥"],
			  ["🡠", None, "🡢"],
			  ["🡧", "🡣", "🡦"]]

	return arrows[1-a][1-b]


def king_walk(G):
	n = len(G)
	Q = Queue()

	cost = [[-1]*n for _ in range(n)]
	direction = [['0']*n for _ in range(n)]

	cost[0][0] = G[0][0]
	Q.put((0,0,0))

	while not Q.empty():
		i, j, p = Q.get()
		if p>1:
			Q.put((i, j, p-1))
		else:
			for mi, mj in moves(i, j, n):
				if cost[mi][mj]<0:
					Q.put((mi, mj, G[mi][mj]))
					cost[mi][mj] = cost[i][j] + G[mi][mj]
					direction[mi][mj] = dir(mi-i, mj-j)
				elif cost[mi][mj] > cost[i][j] + G[mi][mj]:
					cost[mi][mj] = cost[i][j] + G[mi][mj]
					direction[mi][mj] = dir(mi-i, mj-j)

	print()
	for row in cost:
		print(row)

	print()
	for row in direction:
		print(row)

	return cost[n-1][n-1]


king_walk(T)