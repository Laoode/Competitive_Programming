n = int(input())
lis=[]
los=[]
for _ in range(n):
    a = input()
    b = input()
    for i in range(len(a)):
        if a[i]!=b[i]:
            lis.append('*')
        else:
            lis.append('.')
    
    c = ''.join(lis)
    los.append([a,b,c])
    lis.clear()

for i in los:
    for j in i:
        print(j)
    print()