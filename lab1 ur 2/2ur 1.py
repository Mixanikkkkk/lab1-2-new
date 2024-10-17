from math import *
x=float(input())
last_ch=10000
s=0
i=1
while abs(last_ch)>0.0001:
    s+=(cos(i*x))/(i**2)
    last_ch=(cos(i*x))/(i**2)
    i+=1
print(s)
