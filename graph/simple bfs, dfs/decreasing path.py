from queue import Queue

G = [[0, 0, 3, 0, 2, 9],
	[0, 0, 5, 1, 0, 8],
	[3, 5, 0, 6, 4, 7],
	[0, 1, 6, 0, 0, 0],
	[2, 0, 4, 0, 0, 0],
	[9, 8, 7, 0, 0, 0]]

def malejaca_sciezka(G, x, y):
	# G jako macierz sądziedztwa
	n = len(G)
	Q = Queue()

	Q.put((x, 0))

	while not Q.empty():
		v, kr = Q.get()
		for vn in [i for i in range(n) if G[v][i]>kr]:
			if vn==y:
				return True
			else:
				Q.put((vn, G[v][vn]))

	return False


print(malejaca_sciezka(G, 4, 1))