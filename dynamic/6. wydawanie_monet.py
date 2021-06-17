'''
F[s] - najmniejsza liczba monet do wydania s
F[s] = min( [1 + F[s-nom] for nom in nominały] )
F[0] = 0

F[s] = None jesli nie mozna uzbierac s

'''

def wydawanie(A, suma):
    F = [0]*(suma+1)

    for i in range(1, suma+1):
        lis = [1+ F[i-nom] if (i-nom>=0 and F[i-nom] is not None) else None for nom in A]
        lis = [n for n in lis if n is not None]

        if lis!=[]:
            F[i] = min(lis)
        else:
            F[i] = None
    
    print(F)
    return F[suma]


A = [2, 5, 8]
suma = 21
print(wydawanie(A, suma))