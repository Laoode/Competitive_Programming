n = int(input())
lis = []
inp1 = list(map(int, input().split()))
inp2 = list(map(int, input().split()))

for i in inp1:
    if i not in inp2:
        lis.append(i)

print(''.join(map(str, lis)))