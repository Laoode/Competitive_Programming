n = int(input())

lis=[]
for i in range(1,n+1):
    a = int(input())
    if not lis:
        lis.append(a)
    else:
        if lis[0]<a:
            lis.insert(0,a)
        else:
            if a > lis[-1]:
                continue
            else:
                lis.append(a)
print(len(lis))
# it's not compatible with python for this question