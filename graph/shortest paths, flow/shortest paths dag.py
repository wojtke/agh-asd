def top_sort(G):
	# G jako lista sądziedztwa
	def dfs_visit(G, v):
		nonlocal time
		visited[v] = True

		for vn, _ in G[v]:
			if not visited[vn]:
				dfs_visit(G, vn)

		result[n-1-time] = v
		time+=1

	n = len(G)

	visited = [False]*n
	result = [None]*n
	time = 0

	for v in range(n):
		if not visited[v]:
			dfs_visit(G, v)

	return result


def shortest_dag(G, s): #adj list
	def relax(v, vn, w):
		if dist[vn] > dist[v] + w:
			dist[vn] = dist[v] + w
			parent[vn] = v

	tsorted = top_sort(G)
	parent = [None]*len(G)
	dist = [float('inf')]*len(G)

	i = 0
	while tsorted[i]!=s:
		i+=1

	dist[s] = 0

	for v in tsorted[i:]:
		for vn, w in G[v]:
			relax(v, vn, w)

	return dist

G = [ 
	[(1, 5), (2, 1)],
	[(4,5)],
	[(1, 12)],
	[],
	[(3, 12),(5, 123), (6,12)],
	[],
	[],
	]

d = shortest_dag(G, 1)

print(d)

