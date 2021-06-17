K = [[123,51324,234,12,55],
	[213,424,214,142,554,12333],
	[2,4,24124,1442,554124,1,1,123]]

def steal(K):
	K = [sorted(row) for row in K]
	sums = [sum(row) for row in K]

	delta = max(sums[1:])-sums[0]
	count=0

	while delta>0:
		best_i = 0
		best_d = 0
		for i in range(1, len(K)):
			d = sums[0]+K[i][-1] - max(sums[1:i] + [sums[i]-K[i][-1]] + sums[i+1:])
			if d>best_d:
				best_d = d
				best_i = i

		sums[best_i]-=K[best_i][-1]
		sums[0]+=K[best_i][-1]
		K[best_i].pop()

		delta -= best_d
		count+=1
		
	return count




print(steal(K))

