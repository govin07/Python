import numpy as np

a = np.random.randint(1,100,24).reshape(6,4)

a < 50
# print(a)

# print(a[(a % 2 == 0) & (a< 50)])


# broadcasting

g = np.arange(12).reshape(4,3)
b = np.arange(3)

print(g)
print(b)

print(g+b)