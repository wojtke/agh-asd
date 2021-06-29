'''
Given coins of face value G[i] find the least amount of coins with total value v.

F[s] - least amount of coins with total value s
F[s] = min( [1 + F[s-g] for g in G] )
F[0] = 0

F[s] = None if there is no combination of coin with total value s

'''

def coins(G, v):
    F = [0]*(v+1)

    for i in range(1, v+1):
        lis = [1+ F[i-g] for g in G if (i-g>=0 and F[i-g] is not None) ]

        if lis!=[]:
            F[i] = min(lis)
        else:
            F[i] = None
    
    print(F)
    return F[v]

# example

A = [2, 5, 8]
suma = 21
print(coins(A, suma))