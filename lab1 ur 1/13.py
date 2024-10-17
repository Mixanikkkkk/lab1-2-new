for x in range(-15, -9):
    x/=10
    y=1
    print("{0:8.1f} {1:<8.1f}".format(x, y))
for x in range(-9, 11):
    x/=10
    y=-x
    print("{0:8.1f} {1:<8.1f}".format(x,y))
for x in range(11, 16):
    x/=10
    y=-1
    print("{0:8.1f} {1:<8.1f}".format(x,y))