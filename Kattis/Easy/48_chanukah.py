n = int(input())
lis=[]
for i in range(n):
    a,n =map(int,input().split())
    lis.append(a)
    b = int((n*(n+1)/2)+n)
    lis.append(b)
x = len(lis)

for i in range(0, x, 2):
    print(f"{lis[i]} {lis[i+1]}")
