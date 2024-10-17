s=0
x=float(input())
last_ch=1000
n=0
while abs(last_ch)>0.0001:
    s+=x**(n*2)
    last_ch=x**(n*2)
    n+=1
print(s)