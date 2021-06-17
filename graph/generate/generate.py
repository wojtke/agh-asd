from graph import Graph, Presets


G = Graph(n=10, density=0.5, directed=False)

print(G.is_connected())

print("[")
for row in G.get():
	print(row,",", sep="")
print("]")
print()

print("[")
for b in G.get_bit():
	print(bin(b),",", sep="")
print("]")
print()

"""
G = G.to_adj_list()

print("[")
for x in G.get():
	print(x,",", sep="")
print("]")
"""