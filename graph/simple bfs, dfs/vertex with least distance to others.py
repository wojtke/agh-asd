from queue import Queue

def bfs_dist(G, s):
	# G jako lista sądziedztwa
	n = len(G)
	Q = Queue()

	visited = [False]*n
	depth = [-1]*n

	visited[s] = True
	depth[s] = 0
	Q.put(s)

	while not Q.empty():
		v = Q.get()
		for vn, w in G[v]:
			if not visited[vn]:
				visited[vn] = True
				depth[vn] = depth[v] + w

				Q.put(vn)

	return depth


def best_root(G):
	n=len(G)
	dist = bfs_dist(G, 0)

	v1 = max(range(n), key = lambda x:dist[x])
	dist1 = bfs_dist(G, v1)
	v2 = max(range(n), key = lambda x:dist1[x])
	dist2 = bfs_dist(G, v2)

	# v1 and v2 are end verticies of a diameter

	max_dist = [max(dist1[i], dist2[i]) for i in range(n)]

	best_root = min(range(n), key=lambda x:max_dist[x])

	return best_root, max_dist[best_root]


G = [
	[(4, 15)],
	[(2, 8), (5, 20), (8, 5)],
	[(1, 8), (6, 19)],
	[(4, 8), (6, 16)],
	[(0, 15), (3, 8)],
	[(1, 20)],
	[(2, 19), (3, 16), (7, 6)],
	[(6, 6)],
	[(1, 5), (9, 1)],
	[(8, 1)],
	]

print(best_root(G))
