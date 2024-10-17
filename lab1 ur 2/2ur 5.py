n=int(input())
m=int(input())
c=0
while n>=m:
    n-=m
    c+=1
print(f'Частное = {c}, остаток = {n}')
