# F[i][j] - min liczba krokow wskoczyc na i-te miejsce majac j energii w zapasie

A = [2,1,1,0,3,2,0,0,5,1,0,2,0,1,0,1,0,1]

def zaba(A):
	max_energia = sum(A)
	n = len(A)

	F = [[None]*(max_energia+1) for _ in range(n)]

	F[0][0] = 0

	def f(i, j):
		j = max(0, j)
		print(i, j)
		if F[i][j] != None:
			return F[i][j]

		best = None
		k=1
		while k<=i and f(i-k, j+k-A[i-k]) != None:
			case =  1 + f(i-k, j+k-A[i-k])
			if best == None or best>case:
				best = case
			k+=1
		F[i][j] = best

		return F[i][j]

	return f(n-1, 0)


zaba(A)