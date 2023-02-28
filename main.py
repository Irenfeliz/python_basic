from math import *

n = int(input())
k = 0

for i in range(n):
    k += 1 / (i + 1)
    j = k - log(n)

print(j)