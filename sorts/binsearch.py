
def binsearch(T, x, i=0, j=None):
	#[i,j)
	j = j or len(T)

	mid = (i+j)//2

	if j-i<2:
		if T[mid]!=x:
			return None
		else:
			return mid

	elif T[mid]==x:
		return binsearch(T, x, i, mid) or mid

	elif T[mid]>x:
		return binsearch(T, x, i, mid)

	elif T[mid]<x:
		return binsearch(T, x, mid+1, j)



T = [0, 1, 11, 12, 12, 12, 12, 12, 12, 13]


for i, x in enumerate(T):
	print(i, x, binsearch(T, x))