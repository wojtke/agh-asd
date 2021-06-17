G = [ 
	[1, 2],
	[0, 2],
	[0, 3],
	[],
	]

G = [[0,1,1,0,0,0],
	[1,0,1,0,0,1],
	[1,1,0,0,0,1],
	[0,0,0,0,0,1],
	[0,0,0,0,0,1],
	[0,1,1,1,1,0]]

def dfs_adj_list(G):
	# G jako lista sądziedztwa
	def dfs_visit(G, v):
		visited[v] = True

		for vn in G[v]:
			if not visited[vn]:
				dfs_visit(G, vn)

	n = len(G)

	visited = [False]*n

	for v in range(n):
		if not visited[v]:
			dfs_visit(G, v)



def dfs_adj_matrix(G):
	# G jako macierz sąsiedztwa
	def dfs_visit(G, v):
		visited[v] = True

		for vn in [i for i in range(n) if G[v][i]==1]:
			if not visited[vn]:
				dfs_visit(G, vn)

	n = len(G)
	visited = [False]*n

	for v in range(n):
		if not visited[v]:
			dfs_visit(G, v)

