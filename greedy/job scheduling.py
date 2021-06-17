D = [1,2,5,2,6,7,4,32,2,4,5,3,5] #termin
G = [1,5,7,3,8,2,8,3,44,3,6,2,5] #profit


def job_scheduling(D, G):
	T = [[i, D[i], G[i]] for i in range(len(D))]

	T.sort(key = lambda x: x[2])

	end = max(T, key = lambda x: x[1])[1]

	schedule = [None]*(end+1)

	for i, deadline, profit in T:
		while schedule[deadline] is not None and deadline>=0:
			deadline-=1
		schedule[deadline]=i

	return [x for x in schedule if x is not None]

print( job_scheduling(D, G) )
