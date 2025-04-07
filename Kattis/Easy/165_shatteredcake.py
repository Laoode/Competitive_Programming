W=int(input())
N=int(input())


lis=[]
for _ in range(N):
    wi,li= map(int, input().split())
    form=wi*li
    lis.append(form)

L=sum(lis)/W
print(int(L))