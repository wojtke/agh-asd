from collections import deque

G= [[None, 0, None, None, None, None, None, 5, None],
    [0, None, 1, None, None, None, None, 0, None],
    [None, 1, None, 1, None, 0, None, None, 1],
    [None, None, 1, None, 1, 0, None, None, None],
    [None, None, None, 1, None, 1, None, None, None],
    [None, None, 0, 1, 1, None, 0, None, None],
    [None, None, None, None, None, 1, None, 1, 0],
    [0, 0, None, None, None, None, 1, None, 1],
    [None, None, 1, None, None, None, 0, 1, None]]


def shortest_01(G, x, y):
	# G jako macierz sądziedztwa
	n = len(G)
	Q = deque([x])

	cost = [None]*n
	parent = [None]*n

	cost[x] = 0

	while len(Q)>0:
		v = Q.popleft()
		for vn, k in [(i, G[v][i]) for i in range(n) if G[v][i] is not None]:
			c = cost[v]+k
			if cost[vn] is None or cost[vn]>c:
				parent[vn] = v
				cost[vn] = c

				if k==1:
					Q.append(vn)
				elif k==0:
					Q.appendleft(vn)




	if cost[y] is not None:
		path = []
		p = y
		while p is not None:
			path.append(p)
			p = parent[p]
		print(path[::-1])

		return cost[y]
	else:
		return -1

print(shortest_01(G, 0, 8))


