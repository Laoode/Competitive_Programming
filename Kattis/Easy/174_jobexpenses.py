n=int(input())
inp=list(map(int, input().split()))
lis=[]
for i in inp:
    if i<0:
        lis.append(i)
print(abs(sum(lis)))