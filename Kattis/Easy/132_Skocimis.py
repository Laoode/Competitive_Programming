a,b,c = map(int, input().split())
lis = [b-a,c-b]
if lis[0]>lis[1]:
    maks = lis[0]
else:
    maks = lis[1]

steps = maks-1

print(steps)