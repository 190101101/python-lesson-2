import numpy as np

#
p1 = np.array([
	range(1, 4),
	range(4, 7),
	range(7, 10),
])

print(p1)
print(p1.ndim)


p2 = np.array([
	[
		[1, 2, 3], 
		[4, 5, 6]
	], 
	[
		[1, 2, 3], 
		[4, 5, 6]
	]
])
print(p2)
print(p2.ndim)
