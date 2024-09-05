n = int(input())
lis = []
for _ in range(n):
    inp = int(input())
    lis.append(inp)
    
if len(lis)%2==1:
    print('still running')
else:
    total = 0
    for i in range(0, len(lis), 2):
        start = lis[i]
        stop = lis[i+1]
        total += stop-start
    print(total)
            