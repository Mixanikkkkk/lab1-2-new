x=float(input())
from math import *
s=0
for i in range(0, 10):
    s+=cos((i+1)*x)/(x**i)
print(s)
