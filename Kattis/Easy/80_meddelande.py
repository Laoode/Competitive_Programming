n,m = list(map(int, input().split()))
lis=[]
for i in range(n):
    inp = input()
    for j in inp:
        if j.isalpha():
            lis.append(j)

print(''.join(lis))