from queue import Queue

G = [[0, 5, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 44, 0, 0],
    [0, 12, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 19, 9],
    [0, 0, 0, 123, 0, 313, 12],
    [0, 6, 0, 0, 0, 0, 0],
    [0, 22, 0, 0, 0, 0, 0]]


S = [(0, 15), (1, 40)]

T = [(5, 25), (4, 20)]

def max_flow_multi(G, S, T):
    n = len(G)

    G.append([0]*n)
    G.append([0]*n)
    for i in range(n+2):
        G[i].append(0)
        G[i].append(0)

    for v, w in S:
        G[n][v]  = w 
    
    for v, w in T:
        G[v][n+1]  = w 


    flow, F = max_flow(G, n, n+1)

    return flow



def max_flow(G, s, t): # edmonds karp
    def res(v, u):
        if G[v][u]:
            return G[v][u] - F[v][u]
        if G[u][v]:
            return F[u][v]
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
                p = parent[p]

        else:
            break

    flow = sum(F[s])

    return flow, F

        
print(max_flow_multi(G, S, T))

