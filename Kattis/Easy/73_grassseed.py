z =float(input())
x =int(input())
lis = []
for i in range(x):
    a = list(map(float, input().split()))
    b = a[0]*a[1]
    lis.append(b)
c = sum(lis)

total = c*z

print(f'{total:.7f}')