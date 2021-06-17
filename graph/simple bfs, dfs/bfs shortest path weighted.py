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


def shortest_path(G, s, f):
	# G jako macierz sądziedztwa
	n = len(G)
	Q = Queue()

	min_path = [-1]*n

	min_path[s] = 0

	Q.put(s)

	while not Q.empty():
		v = Q.get()
		for vn in [i for i in range(n) if G[v][i]>0]:
			if min_path[vn]<0 or min_path[vn]> min_path[v]+G[v][vn]:
				Q.put(vn)
				min_path[vn] = min_path[v] + G[v][vn]

	print(min_path)
	return min_path[f]

print(shortest_path(G, 0, 8))


