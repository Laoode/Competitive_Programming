inpt= input()

lis=[]

for i in range(len(inpt)):
    if inpt[i]=='a':
        for j in range(i,len(inpt)):
            lis.append(inpt[j])
        break
    else:
        None
a ="".join(map(str,lis))
print(a)