inp = int(input())
lis=[]
for i in range(inp):
    n = int(input())
    lis.append(n)

for j in lis:
    if j%2==0:
        print(f"{j} is even")
    else:
        print(f"{j} is odd")