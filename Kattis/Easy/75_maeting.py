a,b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
lis = []
for i in range(len(c)):
    if c[i] in d:
        lis.append(c[i])
    else:
        None

a =" ".join(map(str,lis))
print(a)