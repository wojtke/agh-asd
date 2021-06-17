A = [2,5,2,6,6,8,4,8,4,7,6,4]

# f(i) - najwiekszy zysk ze scinki drzew na obszarze do i-tego drzewa
# f(i) = max(A[i] + f(i-2), f(i-1))

def forest(A):
	F = [0]*len(A)
	P = [0]*len(A)

	F[0]=A[0]
	F[1]=max(A[0], A[1])

	P[0]=2
	if A[0]>A[1]:
		P[1] = 1
	else:
		P[1] = 2

	for i in range(2, len(A)):
		F[i] = max(A[i] + F[i-2], F[i-1])
		if A[i] + F[i-2]>F[i-1]:
			P[i] = 2
		else:
			P[i] = 1


	# odzyskiwanie wyniku, w tym przypadku sprawdzenie czy sumuje sie dobrze
	suma = 0
	i = len(A)-1
	while i>=0:
		if P[i]==2:
			suma+=A[i]
			i-=2
		else:
			i-=1

	print(suma)

	return F[len(A)-1]


print(forest(A))