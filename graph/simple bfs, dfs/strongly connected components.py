G = [ 
	[1, 2],
	[4],
	[1],
	[2],
	[3,5,6],
	[],
	[],
	]


def sss(G):
	# G jako lista sądziedztwa
	def dfs_visit_1(G, v):
		visited[v] = True

		for vn in G[v]:
			Gt[vn].append(v)
			if not visited[vn]:
				dfs_visit_1(G, vn)

		stack.append(v)

	def dfs_visit_2(G, v):
		visited[v] = True
		result[-1].append(v)

		for vn in G[v]:
			if not visited[vn]:
				dfs_visit_2(G, vn)


	n = len(G)

	visited = [False]*n
	stack = []

	# transpozycja G
	Gt = [[] for _ in range(n)]

	for v in range(n):
		if not visited[v]:
			dfs_visit_1(G, v)

	visited = [False]*n
	result = []
	while len(stack)>0:
		result.append([])
		dfs_visit_2(Gt, stack.pop())

	return result


print(sss(G))