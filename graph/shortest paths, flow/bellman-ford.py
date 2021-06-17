def bellman_ford(G, s):
    def relax(v, u, w):
        if dist[u] > dist[v] + w:
            dist[u] = dist[v] + w
            parent[u] = v

    n = len(G)

    edge_list = []
    for i in range(n):
        for j in range(n):
            if G[i][j]!=0:
                edge_list.append( [i, j, G[i][j]] )


    dist = [float('inf')]*n
    parent = [None]*n
    dist[s]=0

    # relax
    for _ in range(n-1):
        for v, u, w in edge_list:
            relax(v, u, w)

    # check for negative cycles

    for v, u, w in edge_list:
        if dist[v] + w < dist[u]:
            print("has negative cycle")

    return dist, parent


    
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

print(bellman_ford(G, 0))