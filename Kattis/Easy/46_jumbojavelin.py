n = int(input())
lis=[]
for i in range(n):
    inp = int(input())
    lis.append(inp)
a=sum(lis)

total=a-n+1
print(total)