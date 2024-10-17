from math import *
s=0
for i in range(1, 7):
    s+=(((-1)**i)*(5**i))/factorial(i)
print(s)