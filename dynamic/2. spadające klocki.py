A = [(1,5), (2,7), (1,2), (4,6), (1,4), (2,5), (3,4)]


def klocki(A):

	n = len(A)
	F = [-1]*n
	F[0] = 0

	# f(i): # ile min klockow trzeba usunac zeby ustawic i pierwszych 
	
	for i in range(1, n):
		best = i
		j = 1
		while j<i and j<best:
			case = F[i-j] + j
			if A[i-j][0]<= A[i][0] and A[i-j][1]>= A[i][1]:
				case-=1

			if best>case:
				best = case

			j+=1
		F[i] = best

	print(F)

	return F[n-1]

print(klocki(A))