t = int(input())
lis = []
for i in range(t):
    n = int(input())
    fac = 1
    for j in range(1,n+1):
        fac*=j
    lis.append(fac)

for k in lis:
    k = str(k)
    print(k[-1])