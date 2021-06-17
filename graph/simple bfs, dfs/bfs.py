from queue import Queue

G = [ 
	[1, 2],
	[0, 2],
	[0, 3],
	[],
	]


def bfs_adj_list(G, s):
	# G jako lista sądziedztwa
	n = len(G)
	Q = Queue()

	visited = [False]*n
	depth = [-1]*n
	parent = [None]*n

	visited[s] = True
	depth[s] = 0
	Q.put(s)

	while not Q.empty():
		v = Q.get()
		for vn in G[v]:
			if not visited[vn]:
				visited[vn] = True
				depth[vn] = depth[v] + 1
				parent[vn] = v

				Q.put(vn)

	return depth, parent

  