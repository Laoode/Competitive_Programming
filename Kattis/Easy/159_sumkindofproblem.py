p = int(input())
data=[]
for _ in range(p):
    d,n = map(int, input().split())
    s1=n*(n+1)//2
    s2=n**2
    s3=n*(n+1)
    lis=[d, s1, s2, s3]
    data.append(lis)

for i in data:
    print(*i)