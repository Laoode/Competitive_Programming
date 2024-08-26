inp = input()
lis = []
for i in inp:
    if not lis or i != lis[-1]:
        lis.append(i)
print(''.join(lis))
