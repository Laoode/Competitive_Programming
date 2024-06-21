n = int(input())
lis = []
cold = list(map(str, input().split()))

for i in cold:
    i = int(i)
    if i<0:
        lis.append(i)

print(len(lis))