ch1, ch2 = 1, 2
zn1, zn2 = 1, 1
ch3 = ch1+ch2
zn3 = zn1+zn2
for i in range(3):
    print(ch3/zn3, end=' ')
    ch1=ch2
    ch2=ch3
    zn1=zn2
    zn2=zn3
    ch3 = ch1 + ch2
    zn3 = zn1 + zn2
