n,k = map(int, input().split())
n_sec = list(map(int, input().split()))
q = n//k

lis=[]
for i in range(1, q + 1):
    form  = i * k - 1
    lis.append(n_sec[form])
print(*lis)  