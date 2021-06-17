from queue import Queue

G = [[0, 0, 12, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 20, 0, 19, 1],
    [12, 3, 0, 9, 9, 19, 0, 19, 0, 17],
    [0, 0, 9, 0, 0, 6, 0, 5, 14, 5],
    [0, 0, 9, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 19, 6, 0, 0, 6, 0, 16, 0],
    [0, 20, 0, 0, 0, 6, 0, 4, 0, 3],
    [0, 0, 19, 5, 8, 0, 4, 0, 12, 0],
    [0, 19, 0, 14, 0, 16, 0, 12, 0, 10],
    [0, 1, 17, 5, 0, 0, 3, 0, 10, 0],]


def max_flow(G, s, t): # edmonds karp
    def res(v, u):
        if G[v][u]:
            return G[v][u] - F[v][u]
        return 0

    n = len(G)
    F = [[0]*n for _ in range(n)]

    while True:
        Q = Queue()

        visited = [False]*n
        parent = [None]*n
        Q.put(s)

        while not Q.empty():
            v = Q.get()
            if v == t:
                break
            for u in range(n):
                if res(v, u)>0 and not visited[u]:
                    visited[u] = True
                    parent[u] = v 
                
                    Q.put(u)

        if parent[t] is not None:
            # znajdowanie min_res
            min_res = float('inf')
            p = t
            while p!=s:
                min_res = min(min_res, res(parent[p], p))
                p = parent[p]

            # updatowanie wartosci flow
            p = t
            while p!=s:
                F[parent[p]][p] += min_res
                F[p][parent[p]] -= min_res
                p = parent[p]

        else:
            break

    flow = sum(F[s])

    return flow, F

        
flow, F = max_flow(G, 0, 4)

for row in F:
    print(row)

