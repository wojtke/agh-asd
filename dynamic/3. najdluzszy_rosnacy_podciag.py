"""

F[i][j] - najdluzszy podciag rosnacy przed i-tym elementu, przedluzajacy podciag kończący sie przed j-tym elementem

F[i][j] = 1 + F[i-1][j-1] if A[i]>A[j]
F[i][j] = max(F[i-1][j], F[i][j-1]) wpp

"""

A = [8,5,34,2,43,75,2,57]

n = len(A)

F = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
	for j in range(1, n+1):
		if A[i-1]>A[j-1]:
			F[i][j] = 1 + F[i-1][j-1]
		else:
			F[i][j] = max(F[i-1][j], F[i][j-1])

print(F[n][n])