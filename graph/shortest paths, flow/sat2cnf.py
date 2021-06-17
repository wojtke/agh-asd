
lit = [(1,2), (-1,-2), (1, -2), (-1, 2)]

def sat2cnf(lit, n):
	G = [[] for _ in range(2*n+1)]
	for a, b in lit:
		if not n+b in G[n-a]:
			G[n-a].append(n+b)
		if not n+a in G[n-b]:
			G[n-b].append(n+a)

	S = scc(G)

	print(S)

	for s in S:
		val = [None]*(n+1)
		for v in s:
			if val[abs(n-v)] is not None and val[abs(n-v)]!= (v>n):
				return False
			else:
				val[abs(v-n)] = (v>n)

	return True

def scc(G):
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


print(sat2cnf(lit, 4))
