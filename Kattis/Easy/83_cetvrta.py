lisa = []
lisb = []
for _ in range(3):
    a,b = list(map(int, input().split()))
    lisa.append(a)
    lisb.append(b)
lis = []
for i in lisa:
    counter = lisa.count(i)
    if counter == 1:
        lis.append(i)
for i in lisb:
    counter = lisb.count(i)
    if counter == 1:
        lis.append(i)
        
print(' '.join(map(str, lis)))
    