sum=0
for x in range(1, 7):
    s=1
    for i in range(1, x+1):
        s*=i
    sum+=s
print(sum)