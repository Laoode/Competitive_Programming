inp = input().split()
inp = map(str.upper, inp)
inp = list(inp)
lis = []
for i in inp:
    if i not in lis:
        lis.append(i)
    else:
        None
if len(lis) == len(inp):
    print('yes')
else:
    print('no')