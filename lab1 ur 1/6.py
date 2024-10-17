for x in range(-8, 9):
    x/=2
    y = 0.5*(x**2)-7*x
    print("{0:8.1f} {1:<8.3f}".format(x,y))