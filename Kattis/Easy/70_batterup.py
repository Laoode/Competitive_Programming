n = int(input())

inp = list(map(int, input().split()))
los = []
for i in inp:
    if i >= 0:
        los.append(i)
    else:
        None

a =sum(los)
b = len(los)

total = a/b
print(total)