"""

F[i][k] - maksymalna wartosc podzialu tablicy (pierwsze i wartosci), na k podciagow

F[i][k]  = max( [ min( F[i-x], sum(A[i-x:i]) ) for x in range(i+1)) ] 

"""

A = [5,6,1,3,12,1,6,5,8,11,7]
k = 3


F = [[-1]*(k+1) for _ in range(len(A)+1)]
F = [[-1]*(k+1) for _ in range(len(A)+1)]

def f(i, k):
	if F[i][k]>=0:
		return F[i][k]

	if i<k:
		F[i][k] = 0
	elif k==1:
		F[i][k] = sum(A[:i])
	else:
		F[i][k] = max( [ min( f(i-x, k-1), sum(A[i-x:i]) ) for x in range(i) ] )

	return F[i][k]

print(f(len(A),k))

print(F)


