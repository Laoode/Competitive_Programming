inp = input()
los=[]
for i in inp:
    if i.isalpha():
        los.append(1)
else:
    None
print(sum(los))