 G = [ 
	[1, 2],
	[4],
	[1],
	[],
	[3,5,6],
	[],
	[],
	]


def top_sort(G):
	# G jako lista sądziedztwa
	def dfs_visit(G, v):
		nonlocal time
		visited[v] = True
   
		for vn in G[v]:
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


print(top_sort(G))





