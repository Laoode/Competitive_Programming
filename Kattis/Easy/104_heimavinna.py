n = input()
lis = []
current_num = ''
for i in n:
    if i.isdigit():
        current_num += i
    elif i == '-':
        if current_num:
            lis.append(int(current_num))
            current_num = ''
        lis.append(i)
    elif i == ';':
        if current_num:
            lis.append(int(current_num))
            current_num = ''
        
if current_num:
    lis.append(int(current_num))
    
los = []
for j in range(len(lis)):
    if lis[j] == '-':
        start = int(lis[j - 1])
        end = int(lis[j + 1])
        for k in range(start+1,end):
            los.append(k)
    else:
        los.append(lis[j])

print(len(los))