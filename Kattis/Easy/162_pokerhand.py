inp = list(map(str, input().split()))
lis=[]
lis_count={}
for i in inp:
    lis.append(i[0])
    if i[0] in lis_count:
        lis_count[i[0]]+=1
    else:
        lis_count[i[0]]=1

print(max(lis_count.values()))