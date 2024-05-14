n,x = map(int, input().split())
lis =[]
for i in range(n):
    s = int(input())
    lis.append(s)
a = sum(lis)

if a == x:
    print("Jebb")
else:
    print("Neibb")