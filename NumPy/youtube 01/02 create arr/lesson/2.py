import numpy as np

#
p1 = np.array([1,2,5000, 1000], dtype='int8')

print(p1)


# print(np.complex64(p1))

p2 = np.complex64(p1)

p3 = np.int32(p2)
print(p3)