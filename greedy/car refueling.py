P = [2,5,3,3,10,2]
S = [1,3,7,12,13,17]
t = 20
L = 10

def min_liczba_tank(S, t, L):
	tankowan = 0
	i=0
	bak = L
	dist = 0
	while i<len(S) and S[i]<t:
		if S[i]-dist <= bak:
			bak-=S[i]-dist
			dist = S[i]
			i+=1
		elif S[i]-dist <=L:
			bak = L - (S[i]-dist)
			tankowan+=1
			dist = S[i]
			i+=1
		else:
			return -1

	if t-dist <= bak:
		return tankowan
	elif t-dist <=L:
		return tankowan+1
	else:
		return -1




def min_koszt_tank(P, S, t, L):
	# dynamiczny
	# zakladam, ze t jest dalej niz S[-1]
	# F - min koszt dotarcia do i, tak ze w baku jest minimum j
	n = len(S)
	F = [[None]*(L+1) for _ in range(n)]

	for j in range(L+1-S[0]):
		F[0][j] = 0

	for i in range(1, n):
		for j in range(L+1):
			best = None
			if j + S[i] - S[i-1] <=L:
				k = 0
				while k<=L:
					if F[i-1][k] is not None:
						case = F[i-1][k] + P[i-1]*max(0, (j + S[i] - S[i-1] - k) )
					if best==None or case<best:
						best = case
					k+=1
			F[i][j] = best

	best = None
	for j, x in enumerate(F[n-1]):
		if x is not None:
			case = x + P[n-1]*max(0, (t-S[n-1] - j))
			if best==None or case<best:
				best = case

	return best

	

def min_koszt_do_pelna(P, S, t, L):
	# zachlanny
	# zakladam ze rozwiazanie istnieje
	
	n = len(S)
	bak = L - S[0]
	koszt = 0

	i=0
	while S[i]+L<t:
		j=0
		min_cena = P[i]
		while i+j<n and S[i+j]-S[i]<=bak:
			if P[i+j]<min_cena:
				min_cena = P[i+j]
			j+=1
		if P[i] == min_cena:
			koszt+=min_cena*(L-bak)
			bak = L

		bak -= S[i+1] - S[i]
		i+=1

	if S[i]+bak>=t:
		return koszt
	else:
		cases = [P[i+j]*(L - bak + S[i+j] - S[i]) for j in range(n-i) if (bak-S[i+j]+S[i])>=0]
		return koszt + min(cases)



print(min_liczba_tank(S, t, L))
print(min_koszt_tank(P, S, t, L))
print(min_koszt_do_pelna(P, S, t, L))