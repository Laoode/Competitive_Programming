n,m=map(int, input().split())

x = 4*n
y = 3*m
con = x+y
if con%2==0:
    print("possible")
else:
    print("impossible")