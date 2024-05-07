name=input()
singkat=name[0]
liss=[singkat]
for i in range(len(name)):
    for j in name[i]:
        if name[i]=='-':
            liss.append(name[i+1])
    
jadi=''.join(liss)            
print(jadi.upper())