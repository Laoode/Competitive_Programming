inpt= input()
inpt =inpt.lower()
lis=[]

for i in inpt:
    if i == "a" or i=="i" or i =="u" or i == "e" or i == "o":
        lis.append(i)

print(len(lis))