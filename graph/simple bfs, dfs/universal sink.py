
from random import randint
'''
n=4
G = [[randint(0,1) if i!=j else 0 for i in range(n)] for j in range(n)]

G = [[0, 1, 1, 1],
	[1, 0, 1, 1],
	[0, 0, 0, 0],
	[0, 1, 1, 0]]

for row in G:
	print(row)
'''

def sink(G):
	n = len(G)

	i, j = 0, 1

	while i<n and j<n:	
		while j<n and G[i][j]==0:
			j+=1
		if j==n:
			break
		i = j
		j+=1

	# i jest kandydatem

	for x in range(n):
		if not (G[i][x] == 0 or i==x):
			return None

	for x in range(n):
		if not (G[x][i] == 1 or i==x):
			return None


	return i


n = 6
while True:
	G = [[randint(0,1) if i!=j else 0 for i in range(n)] for j in range(n)]
	a = sink(G)
	print(a)
	if a is not None:
		break

for row in G:
	print(row)




