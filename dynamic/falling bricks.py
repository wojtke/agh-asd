"""
Problem:
Bricks ( sections (a,b) ) are falling from the sky. Bricks can land on top of each other only if 
upper brick's section is in bottom brick's section.

Find max number of bricks that could land on top of each other creating sort of a tower.
"""

def bricks(A):

	n = len(A)
	F = [-1]*n
	F[0] = 0

	# f(i): # min number of bricks to delete in order to place i first bricks (counting those deleted)
	
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

	return n-F[n-1]

"""
Solution using LIS O(n^2)
"""
def bricks_lis(A):
	def gt(a, b): # a>b? - 'greater than' relation
		# in this case: whether a can land on b?
		return ( b[0]<=a[0] and a[1]<=b[1] )

	n = len(A)
	F = [0]*(n)

	for i in range(n):
		F[i] = max([1+F[k] for k in range(i) if gt(A[i], A[k])] + [1])

	return F[n-1]

# example

A = [(1,5), (2,7), (1,2), (4,6), (1,4), (2,5), (3,4)]

print(bricks_lis(A))
print(bricks(A))