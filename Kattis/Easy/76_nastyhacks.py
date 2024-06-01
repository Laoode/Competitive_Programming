inp = int(input())
lis =[]
for j in range(inp):
    n,i,b = list(map(int, input().split()))
    nilai = i-b
    if nilai>n:
        ad = "advertise"
        lis.append(ad)
    elif nilai < n:
        nod = "do not advertise"
        lis.append(nod)
    else:
        nop = "does not matter"
        lis.append(nop)

for j in lis:
    print(j)
        
    