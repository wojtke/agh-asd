from queue import PriorityQueue

G = [ 
    [(1, 6), (2, 7), (3, 10), (4, 8), (5, 4)],
    [(3, 7), (4, 3)],
    [(1, 5), (3, 8)],
    [(4, 9)],
    [(2, 6)],
    [(2, 1), (3, 1), (4, 6)],
    ]

P = [4,1,55,24,12,9]

def trasa(G, P, D, s):
    def relax(v, vn, bak, new_bak, dist):
        if cost[vn][new_bak-dist] > cost[v][bak] + P[v]*(new_bak-bak):
            cost[vn][new_bak-dist] = cost[v][bak] + P[v]*(new_bak-bak)
            parent[vn][new_bak-dist] = v, bak, dist

    n = len(G)
    Q = PriorityQueue()

    vis = [[False]*(D+1) for _ in range(n)]
    cost = [[float('inf')]*(D+1) for _ in range(n)]
    parent = [[None]*(D+1) for _ in range(n)]

    cost[s][0] = 0
    Q.put( (0, 0, s) )

    while not Q.empty():
        _, bak, v = Q.get()

        if not vis[v][bak]:
            vis[v][bak] = True

            for vn, dist in G[v]:
                for new_bak in range(bak, D+1):
                    if dist<= new_bak:
                        relax(v, vn, bak, new_bak, dist)
                        Q.put( (cost[vn], new_bak-dist, vn) )

    return cost, parent

def print_path(parent, s, t, bak=0):
    path = []
    tanks = []
    fin = t

    while t!=s:
        t, last_bak, dist = parent[t][bak]
        path.append(t)
        tanks.append(bak + dist - last_bak)
        bak = last_bak

    for v, tank in zip(path[::-1], tanks[::-1]):
        print(v, end=" ")
        print(f"({tank})", end=" -> ")
    print(fin)

c, p = trasa(G, P, 10, 0)


for v in range(len(G)):
    print(c[v][0], end=": ")
    print_path(p, 0, v, 5)


