n = int(input())
lis=[]
for i in range(n):
    inp = input()
    lis.append(inp)

los=[]

for i in range(len(lis)):
    if lis[i]=="keys" or lis[i]=="wallet" or lis[i]=="phone":
        los.append(lis[i])

los.sort()

a=["keys","phone","wallet"]

if los==a:
    print("ready")
else:
    for item in a:
        if item not in los:
            print(item)
