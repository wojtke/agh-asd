from queue import PriorityQueue

def dijkstra_adj_matrix(G, s):
    def relax(v, vn):
        if dist[vn] > dist[v] + G[v][vn]:
            dist[vn] = dist[v] + G[v][vn]
            parent[vn] = v

    n = len(G)

    dist = [float('inf')]*n
    parent = [None]*n
    spt = [False]*n
    counter=n

    dist[s] = 0

    while counter>0:

        v = min([i for i in range(n) if not spt[i]], key=lambda v: dist[v])

        if not spt[v]:
            spt[v] = True
            counter-=1

            for vn in [vn for vn in range(n) if G[v][vn]!=0]:
                relax(v, vn)

    return dist, parent



def dijkstra_adj_list(G, s):
    def relax(v, vn, w):
        if dist[vn] > dist[v] + w:
            dist[vn] = dist[v] + w
            parent[vn] = v

    n = len(G)
    Q = PriorityQueue()

    spt = [False]*n
    dist = [float('inf')]*n
    parent = [None]*n
    counter = n

    dist[s] = 0
    Q.put( (0, s) )

    while not Q.empty() and counter>0:
        d, v = Q.get()

        if not spt[v]:
            spt[v] = True
            counter-=1

            for vn, w in G[v]:
                relax(v, vn, w)
                Q.put( (dist[vn], vn) )

    return dist, parent

# Example 

G1 = [ 
    [(1, 6), (2, 7), (3, 10), (4, 8), (5, 4)],
    [(3, 7), (4, 3)],
    [(1, 5), (3, 8)],
    [(4, 9)],
    [(2, 6)],
    [(2, 1), (3, 1), (4, 6)],
    ]


G2 = [[0, 6, 7, 10, 8, 4],
    [0, 0, 0, 7, 3, 0],
    [0, 5, 0, 8, 0, 0],
    [0, 0, 0, 0, 9, 0],
    [0, 0, 6, 0, 0, 0],
    [0, 0, 1, 1, 6, 0]]


G = [[0, 0, 20, 1, 2, 0, 19, 0, 19, 0],
    [0, 0, 3, 0, 18, 0, 18, 0, 0, 0],
    [20, 3, 0, 16, 0, 0, 6, 0, 6, 0],
    [1, 0, 16, 0, 18, 0, 20, 10, 0, 0],
    [2, 18, 0, 18, 0, 20, 0, 0, 0, 0],
    [0, 0, 0, 0, 20, 0, 9, 0, 0, 8],
    [19, 18, 6, 20, 0, 9, 0, 3, 0, 19],
    [0, 0, 0, 10, 0, 0, 3, 0, 17, 0],
    [19, 0, 6, 0, 0, 0, 0, 17, 0, 0],
    [0, 0, 0, 0, 0, 8, 19, 0, 0, 0],]

print(dijkstra_adj_matrix(G, 0))
'''
a1 = dijkstra_adj_list(G1, 0)
a2 = dijkstra_adj_matrix(G2, 0)

print(a1)
print(a2)
'''





