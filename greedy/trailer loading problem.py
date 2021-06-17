from math import log2

K = 32
W = [2,2,4,2,2,8,8]


def laduj(K, W):

	p = int(log2(max(W)))
	n = int(log2(K)+1)

	w_count = [0]*(p+1)

	for w in W:
		w_count[int(log2(w))]+=1

	zaladowac = []

	while K>=0 and p>=0:
		while K>=2**p and w_count[p]>0:
			K-=2**p
			w_count[p]-=1
			zaladowac.append(2**p)
		p-=1

	return zaladowac

print(sum(laduj(K,W)))