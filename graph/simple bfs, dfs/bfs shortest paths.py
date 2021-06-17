from queue import Queue

G= [[0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]]


def shortest_path(G, x, y):
	# G jako macierz sądziedztwa
	n = len(G)
	Q = Queue()

	parent = [None]*n
	visited = [False]*n

	Q.put(x)
	visited[x] = True

	while not Q.empty():
		v = Q.get()
		print(v)
		for vn in [i for i in range(n) if G[v][i]>0]:
			if not visited[vn]:
				visited[vn] = True
				parent[vn] = v

				Q.put(vn)
	p = y
	path = []
	while p is not None:
		path.append(p)
		p = parent[p]

	if x==path[-1]:
		print(path[::-1])
		return len(path)
	else:
		return -1

print(shortest_path(G, 2, 8))


