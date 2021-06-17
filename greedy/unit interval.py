X = [0.25, 0.5, 1.6]

def pokryj(X):
	X.sort()

	przedzialy = []

	przedzialy.append( (X[0], X[0]+1) )

	for i in range(len(X)):
		if przedzialy[-1][1]<X[i]:
			przedzialy.append( (X[i], X[i]+1) )

	return przedzialy

print(pokryj(X))

