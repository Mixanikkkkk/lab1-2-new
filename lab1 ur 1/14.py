a1, a2 = 1, 1
a3=a1+a2
for i in range(8):
    print(a1, end=' ')
    a1=a2
    a2=a3
    a3=a1+a2