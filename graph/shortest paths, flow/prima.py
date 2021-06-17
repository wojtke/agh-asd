from queue import PriorityQueue

inf = float('inf')

G = [
	[(1, 14), (2, 4), (4, 7), (5, 15), (6, 3)],
	[(0, 14), (5, 13), (6, 4), (7, 17)],
	[(0, 4), (9, 18)],
	[(6, 14), (7, 15)],
	[(0, 7), (5, 11), (6, 14), (8, 14)],
	[(0, 15), (1, 13), (4, 11), (6, 8)],
	[(0, 3), (1, 4), (3, 14), (4, 14), (5, 8), (7, 19), (9, 17)],
	[(1, 17), (3, 15), (6, 19), (8, 6), (9, 13)],
	[(4, 14), (7, 6), (9, 18)],
	[(2, 18), (6, 17), (7, 13), (8, 18)],
	]


# nei dziala
def prim(G):

	n = len(G)
	Q = PriorityQueue()

	parent = [None]*n
	MST = [False]*n 
	counter = n
	mst_sum = 0

	Q.put( (0, 0, None) )

	while not Q.empty() and counter>0:
		w, v, p = Q.get()

		if not MST[v]:
			MST[v]=True
			parent[v] = p
			mst_sum+=w
			counter-=1

			for vn, wn in G[v]:
				Q.put( (wn, vn, v) )

	return parent, mst_sum


a = prim(G)

print(a)