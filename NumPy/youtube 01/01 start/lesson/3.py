import numpy as np

p1 = np.array(range(1, 10))

print(p1)

print(p1[[1, 1, 1, 1]])
print(p1[[True, True, False, False, False, False, True, True, True]])
