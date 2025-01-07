n = int(input())
lis=[]
for _ in range(n):
    t = list(map(int, input().split()))
    impor=0
    for i in range(len(t)):
        if t[i + 1] == 0:
            break
        if t[i+1]>2*(t[i]):
            j = t[i+1]-2*t[i]
            impor+=j
    lis.append(impor)

for i in lis:
    print(i)