n = int(input())
a = input()
lis =[]
for i in a:
    if i.isdigit():
        lis.append(i)
    else:
        lis.append(' ')

joined_string = ''.join(map(str, lis))
split_string = joined_string.split()
los = []
for j in split_string:
    j = int(j)
    los.append(j)
print(max(los))