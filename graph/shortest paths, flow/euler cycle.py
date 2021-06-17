G = [[0,1,1,0,0,0],
	[1,0,1,1,0,1],
	[1,1,0,0,1,1],
	[0,1,0,0,0,1],
	[0,0,1,0,0,1],
	[0,1,1,1,1,0]]

def neighbours(G, v):
  n = len(G)
  for i in range(v):
    if G[i][v] == 1:
      yield i

  for i in range(v, n):
    if G[v][i] == 1:
      yield i

def del_edge(G, v, vn):
  if v<vn:
    G[v][vn]=0
  else:
    G[vn][v]=0

def edge_count(G):
  s = 0
  for row in G:
    s+=sum(row)
  return s//2

def reconstruct(G):
  n = len(G)
  for i in range(1,n):
    for j in range(i):
      G[j][i]=G[i][j]

def has_euler_cycle(G):
  n = len(G)
  for i in range(n):
    if sum(G[i])%2!=0:
      return False
  return True


def euler( G ):
  def dfs_visit(G, v):
    nonlocal time

    for vn in neighbours(G, v):
      del_edge(G, v, vn)
      dfs_visit(G, vn)

    cycle[time] = v
    time += 1

  if not has_euler_cycle(G):
    return None

  cycle = [None]*(edge_count(G)+1)
  time = 0

  dfs_visit(G, 0)

  reconstruct(G)

  return cycle


print(cykl_eulera(G))