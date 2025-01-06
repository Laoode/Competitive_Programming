n = int(input())
lis=[]
for _ in range(n):
    inp = list(map(str, input().split()))
    if inp[0] =='Simon' and inp[1] == 'says':
        mine=[]
        for i in range(2,len(inp)):
            mine.append(inp[i])
        lis.append(mine)
for i in lis:
    print(*i)