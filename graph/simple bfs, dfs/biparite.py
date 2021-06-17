from queue import Queue

G = [ 
	[1],
	[0, 2],
	[0, 3],
	[],
	]

def biparite(G, s):
	# G jako lista sądziedztwa
	n = len(G)
	Q = Queue()

	visited = [False]*n
	color = [None]*n

	visited[s] = True
	color[s] = 0
	Q.put(s)

	while not Q.empty():
		v = Q.get()
		for vn in G[v]:
			if not visited[vn]:
				visited[vn] = True
				color[vn] = (color[v]+1)%2

				Q.put(vn)
			else:
				if color[v]==color[vn]:j
					return False

	return True

a = biparite(G, 0)

print(a)