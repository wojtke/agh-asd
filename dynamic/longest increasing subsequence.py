"""
Find longest increasing subsequence.

O(n^2)
F[i] - longest increasing subsequence ending on ith element
F[0] = 0

"""
def lis(A):
	n = len(A)
	F = [0]*(n)

	for i in range(n):
		F[i] = max([1+F[k] for k in range(i) if A[i]>A[k]] + [1])

	return F[n-1]


"""
Faster: O(nlogn)

F[i] - smallest element that could end increasing subsequence of length i

F[i] has increasing values (Except F[0] is None), thats why we can binsearch it 

"""
def binsearch(T, x, i=0, j=None):
	#[i,j)
	j = j or len(T)

	mid = (i+j)//2

	if j-i<2:
		return mid+1
	if T[mid]>=x:
		return binsearch(T, x, i, mid)
	elif T[mid]<x:
		return binsearch(T, x, mid, j)

def lis_faster(A): 
	F = [None]

	for i in range(len(A)):
		ext = binsearch(F, A[i])

		if ext==len(F):
			F.append(A[i])
		elif i<F[ext]:
			F[ext]=A[i]

	return len(F)-1

# example

A = [8,5,34,2,43,75,2,57]

print(lis_faster(A))
print(lis(A))