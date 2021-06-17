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


def to_edge_list(G):
  edge_list = []
  n = len(G)
  for v in range(n):
    for e in G[v]:
      if v<e[0]:
        edge_list.append( (v, e[0], e[1]))

  return edge_list

class Node:
  def __init__(self):
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

def kruskal(G): # edge list
  G.sort(key = lambda x: x[2])

  MST = []
  mst_sum=0
  n_est = max([max(x[0], x[1]) for x in G])

  nodes = [Node() for _ in range(n_est+1)]

  for v1, v2, w in G:
    n1 = nodes[v1]
    n2 = nodes[v2]

    if find(n1)!=find(n2):
      MST.append( (v1, v2) )
      mst_sum+=w
      union(n1, n2)

  return MST, mst_sum

print(kruskal(to_edge_list(G)))
