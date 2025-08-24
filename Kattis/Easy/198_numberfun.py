n = int(input())
lis=[]
for i in range(n):
    a,b,c= map(int, input().split())
    c = float(c)
    add =a+b
    sub =abs(a-b)
    mul =a*b
    div =a/b
    div1=b/a
    if add==c or sub==c or mul==c or div==c or div1==c:
        lis.append('Possible')
    else:
        lis.append('Impossible')

for i in lis:
    print(i)