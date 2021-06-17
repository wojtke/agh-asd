G = [[1,2,6],
	[0,2],
	[0,1],
	[4,5,6],
	[3,5],
	[3,4],
	[7,8,0,3],
	[6,8],
	[6,7],
	]

def dfs_adj_list(G):
	# G jako lista sądziedztwa
	def dfs_visit(G, v):
		nonlocal time
		visited[v] = True

		lowest = time
		times[v]=time
		time+=1

		for vn in G[v]:
			if not visited[vn]:
				parent[vn]=v
				dfs_visit(G, vn)
				lowest = min(lowest, low[vn])
			elif vn!=parent[v]:
				lowest = min(lowest, times[vn])

		low[v]=lowest

	n = len(G)
	time = 0
	visited = [False]*n
	parent = [None]*n
	low = [None]*n
	times = [None]*n

	for v in range(n):
		if not visited[v]:
			dfs_visit(G, v)

	bridges = []
	for i in range(n):
		if low[i]==times[i] and parent[i] is not None:
			bridges.append([parent[i], i])

	return bridges


print(dfs_adj_list(G))