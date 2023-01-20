import numpy as np

#
p1 = np.array(range(1, 6), 'float64')
print(p1)
# print(np.sctypeDict)

#
p2 = np.array(range(1, 6), 'uintc')
print(p2)

#
p3 = np.array(range(1, 6), 'str_')
print(p3)


print(np.complex(10))
print(np.int16(10.5))