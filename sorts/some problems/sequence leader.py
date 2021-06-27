"""
A number is a sequence leader if occurs more than 50% times in the sequence.
The problem is to find the sequence leader or identify the lack of it.

This method solves it in linear time.
"""

def sequence_leader(T):
	leader_candidate = T[0]
	count = 1

	# identifying the candidate for a sequence leader
	for i in range(1, len(T)):
		if T[i] == leader_candidate:
			count+=1
		else:
			count-=1

		if count==0:
			leader_candidate = T[i]
			count = 1

	# checking if it actually is the sequence leader

	count=0
	for x in T:
		if x==leader_candidate:
			count+=1

	if count>=len(T)/2:
		return leader_candidate
	else:
		return None


T = [2,5,1,4,6,6,2,2,2,4,2,3,1,2,2,2,62,2,2,1337]

print(sequence_leader(T))