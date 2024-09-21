n = int(input())

lis = list(map(int, input().split()))

lis.sort()
lis.reverse()
alice = 0
bob=0
for i in range(len(lis)):
    if i%2 == 0:
        alice+=lis[i]
    else:
        bob+=lis[i]
print(f'{alice} {bob}')