name = input()
lis=[]
nm = reversed(name)
for i in nm:
    lis.append(i)
    if i=='.':
        break
    
print(''.join(reversed(lis)))
