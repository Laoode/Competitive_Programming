n = int(input())

inp = input().split()
lis = []
for kata in inp:
    lis.append(kata[0])

sing = ''.join(lis)

besar = sing.upper()

lus =[]
for i in sing:
    if i in besar:
        lus.append(i)

print(''.join(lus))