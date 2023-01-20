import numpy as np

p1 = np.array(range(1, 10))

print(p1)

p2 = p1.reshape(3,3)
print(p2)

print(p2[1][1])
print(p2[1][2])