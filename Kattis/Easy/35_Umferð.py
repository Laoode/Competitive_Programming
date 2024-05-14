l = int(input())
n = int(input())
lis=[]
for i in range(n):
    inp=input()
    a = list(inp)
    c = a.count(".")
    lis.append(c)

d = sum(lis)

e = l*n
f = d/e

print(f)
