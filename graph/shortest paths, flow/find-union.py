class Node:
	def __init__(self, val):
		self.val = val
		self.rank = 0
		self.parent = self


def find(x):
	if x != x.parent:
		x.parent = find(x.parent)

	return x.parent

def union(x, y):
	x = find(x)
	y = find(y)

	if x==y:
		return

	if x.rank>y.rank:
		y.parent = x
	elif x.rank<y.rank:
		x.parent = y
	else:
		y.parent = x
		x.rank += 1

