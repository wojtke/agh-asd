def dobry_poczatek(G): # lista sasiedztwa
	def dfs_visit(G, v):
		nonlocal time
		nonlocal last

		visited[v] = True

		for vn in G[v]:
			if not visited[vn]:
				 dfs_visit(G, vn)

		time-=1

		if time==0:
			last = v


	last = None
	time = n
	visited = [False]*n

	for v in range(n):
		if not visited[v]:
			dfs_visit(G, v)

	# last jest kandydatem - jesli w grafie są dobre początki to last nim jest

	visited = [False]*n

	dfs_visit(G, last)

	return all(visited)

