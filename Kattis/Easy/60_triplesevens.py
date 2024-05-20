inp = int(input())
lis = []
los=[]
for i in range(3):
    q = map(int, input().split())
    lis.append(q)
    
for y in range(len(lis)):
    for g in lis[y]:
        if g == 7:
            los.append(1)
        
c = sum(los)

if c == 3:
    print(777)
else:
    print(0)