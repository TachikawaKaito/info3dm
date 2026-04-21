import numpy as np

a = np.ones((1,5), dtype=float)
print(a)

a[:,2] = 3.14

b = a.T
print(b)

print(np.dot(a, b))

c = np.random.rand(1,10)
print(c)

d = np.random.normal(10, 2, size=(2,5))
print(d)

print(d[:,2])

print(d[:,2:4])

e = np.random.rand(5,2)
print(np.matmul(d, e))