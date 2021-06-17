from random import randint, random, seed


class Presets:
  dag1 =[ 
        [1, 2],
        [4],
        [1],
        [],
        [3,5,6],
        [],
        [],
        ]

class Graph:
  def __init__(self, G=None, s=None, rep='matrix', n=6, density=0.4, fill=0, weighted=False, directed=True):
    if G is None:
      G = [[fill]*n for _ in range(n)]

      if s:
        seed(s)

      if directed:
        for i in range(n):
          for j in range(n):
              if i!=j and random()>1-density:
                G[i][j]=1

      else:
        for i in range(n):
          for j in range(i):
            if random()>1-density:
              G[i][j]=1
              G[j][i]=1

    self.G = G
    self.n = len(G)
    self.fill = fill
    self.rep = rep
    self.weighted = weighted
    self.directed = directed


  def to_matrix(self): 
    result = [[self.fill]*self.n for _ in range(self.n)]

    if not self.weighted:
      for i in range(self.n):
        for v in self.G[i]:
          result[i][v]=1
    else:
      for i in range(self.n):
        for v, w in self.G[i]:
          result[i][v]=w

    self.rep = 'matrix'

    self.G = result
    return self

  def to_adj_list(self): 
    if not self.weighted:
      result = [[j for j in range(self.n) if self.G[i][j]!=self.fill] for i in range(self.n)]
    else:
      result = [[(j, self.G[i][j]) for j in range(self.n) if self.G[i][j]!=self.fill] for i in range(self.n)]

    self.rep = 'adj_list'

    self.G = result
    return self

  def get_edge_list(self): 
    edge_list = []
    if not self.weighted:
      for i in range(self.n):
        for j in range(i):
          if self.G[i][j]!=self.fill:
            edge_list.append( (i, j))
    else:
      for i in range(self.n):
        for j in range(i):
          if self.G[i][j]!=self.fill:
            edge_list.append( (i, j, G[i][j]))

    return edge_list

  def fill_to_undirected(self):
    for i in range(self.n):
      for j in range(i):
        if self.G[i][j]==self.fill:
          self.G[i][j] = self.G[j][i]
        elif self.G[j][i]==self.fill:
          self.G[j][i] = self. G[i][j]
        else:
          m = max(self.G[i][j], self.G[j][i])
          self.G[i][j] = m
          self.G[j][i] = m

    self.directed = False

    return self

  def clean_2way_edges(self): 
    for i in range(self.n):
      for j in range(i):
        if self.G[i][j]!=self.fill and self.G[j][i]!=self.fill:
          self.G[i][j]=self.fill

    return self

  def add_weights(self, start=1, end=10):
    if self.directed:
      for i in range(self.n):
        for j in range(self.n):
          if self.G[i][j]!=self.fill:
            self.G[i][j]=randint(start, end)
    else:
      for i in range(self.n):
        for j in range(i):
          if self.G[i][j]!=self.fill:
            self.G[i][j]=randint(start, end)
            self.G[j][i] = self.G[i][j]

    self.weighted = True

    return self

  def change_fill(self, new_fill):
    for i in range(self.n):
      for j in range(self.n):
        if self.G[i][j]==self.fill:
          self.G[i][j]=new_fill

    self.fill = new_fill

    return self

  def remove_cycles(self):
    def dfs_visit(v):
      visited[v] = True

      for vn, w  in [(i, self.G[v][i]) for i in range(self.n) if self.G[v][i]!=self.fill]:
        if not visited[vn]:
          G[v][vn] = w
          dfs_visit(vn)

    visited = [False]*self.n
    G = [[self.fill]*self.n for _ in range(self.n)]

    for v in range(self.n):
      if not visited[v]:
        dfs_visit(v)

    self.G = G

    if not self.directed:
      self.fill_to_undirected()

    return self

  def is_connected(self):
    def dfs_visit(v):
      visited[v] = True

      for vn in [i for i in range(self.n) if self.G[v][i]!=self.fill]:
        if not visited[vn]:
          dfs_visit(vn)

    for v in range(self.n):
      visited = [False]*self.n
      dfs_visit(v)

      if all(visited):
        return True
    return False

  def T(self):
    for i in range(self.n):
      for j in range(i):
        self.G[i][j], self.G[j][i] = self.G[j][i], self.G[i][j] 

    return self

  def get_bit(self):
    B = []
    for i in range(self.n):
      B.append( sum([self.G[i][j]<<j for j in range(self.n)]) ) 
    return B

  def get(self):
    return self.G


