"""
Problem: divide sequence into k consecutive subsequences so that minimal sum of a subsequence is maximal.

F[i][k] - max min by dividing first i elements of sequence into k subsequences

F[i][k]  = max( [ min( F[i-x], sum(A[i-x:i]) ) for x in range(i+1)) ] 

"""

def maxmin(A, k):
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

	result = F[len(A)][k]
	# print subsequences
	divs = [len(A)]
	p = len(A)
	while k>1:
		p -= P[p][k]
		divs.append(p)
		k-=1

	s=0
	for i in divs[::-1]:
		print(A[s:i], sum(A[s:i]))
		s=i

	return result

# example
A = [5,6,1,3,12,1,6,5,8,11,7]
k = 3

print(maxmin(A, k))





