"""

F[i][k] - maksymalna wartosc podzialu tablicy (pierwsze i wartosci), na k podciagow

F[i][k]  = max( [ min( F[i-x], sum(A[i-x:i]) ) for x in range(i+1)) ] 


"""
A = [5,6,1,3,12,1,6,5,8,11,7]
k = 3

F = [[0]*(k+1) for _ in range(len(A)+1)]
P = [[0]*(k+1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
	for k in range(1, k+1):
		if i<k:
			F[i][k] = 0
		elif k==1:
			F[i][k] = sum(A[:i])
		else:
			podzialy = [ min( F[i-x][k-1], sum(A[i-x:i]) ) for x in range(i)]
			F[i][k] = max( podzialy )
			P[i][k] = max(range(i), key = lambda x: podzialy[x])


print("Rozwiązanie: ", F[len(A)][k])

indeksy_podzialu = [len(A)]

p = len(A)
while k>1:
	p -= P[p][k]
	indeksy_podzialu.append(p)
	k-=1

s=0
for i in indeksy_podzialu[::-1]:
	print(A[s:i], sum(A[s:i]))
	s=i
