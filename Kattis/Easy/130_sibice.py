n,w,h = map(int, input().split())
lis = []
for _ in range(n):
    inp = int(input())
    lis.append(inp)
pyth = (w**2+h**2)
akar = 0.0
while akar * akar < pyth:
    akar += 0.01 

for i in lis:
    if i <= akar:
        print('DA')
    else:
        print('NE')
    