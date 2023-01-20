import numpy as np


p1 = np.array(range(1, 10))

print(p1[1:5])
print(p1[:5])
print(p1[5:])

print(p1[-3:-1])
print(p1[1:5:2])
print(p1[::2])
print(p1[::3])
print(p1[2::])
