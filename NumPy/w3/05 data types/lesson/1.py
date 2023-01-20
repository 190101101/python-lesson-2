import numpy as np

#
p1 = np.array(range(1, 5))
print(p1.dtype)

#
p2 = np.array(['apple', 'banana', 'cherry'])
print(p2.dtype)

#
p3 = np.array(range(1, 5), dtype='S')
print(p3.dtype)

#
p4 = np.array(range(1, 5), dtype='i4')
print(p4.dtype)

#
p5 = np.array([1.1, 2.1, 3.1])
p6 = p5.astype('i')

print(p6)
print(p6.dtype)

#
p7 = np.array([1.1, 2.1, 3.1])
p8 = p7.astype(int)
print(p8)
print(p8.dtype)

#
p8 = np.array([1, 0, 3])
p9 = p8.astype(bool)
print(p9)
print(p9.dtype)
