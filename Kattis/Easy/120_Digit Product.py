n = int(input())
n = str(n)
lis=[]
for i in n:
    if i != '0':
        lis.append(int(i))
while len(lis)>1:
    total_kali=1
    for i in lis:
        total_kali*=i
    lis = [int(x) for x in str(total_kali)]
print(lis[0])
 