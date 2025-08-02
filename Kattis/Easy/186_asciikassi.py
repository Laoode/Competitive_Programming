n = int(input())
rg = n+2

top_bottom='+'+'-'*n+'+'
middle ='|'+' '*n+'|'
lis=[]
for i in range(1,rg+1):
    if i == 1 or i == rg:
        lis.append(top_bottom)
    else:
        lis.append(middle)

for i in lis:
    print(i)
