"""
Problem:
Find most valuable path in a tree. Path
 F[v] najbardziej wartosciowa sciezka zaczynająca w poddrzewie v, zawierająca v
 F[v] = v.val + max(0, F[child] for child in v.children)

 G[v] najbardziej wartosciowa sciezka zaczynająca w poddrzewie v, niekoniecznie zawierajaca v
 G[v] = max(F[v], G[child] for child in v.children)
"""

class Node:
	def __init__(self, val, children):
		self.val = val
		self.children = children
		self.f = None



def f(v):
	if v.f is not None:
		return v.f
	else:
		v.f = v.val + max([0] + [f(child) for child in v.children])

	return v.f

def g(v):
	if v.g is not None:
		return v.g
	else:
		v.g = max([0, f(v)] + [g(child) for child in v.children])

# example




