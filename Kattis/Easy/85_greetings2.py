inp = input()
lis = []
for i in inp:
    if i == 'e':
        lis.append(i)

res = len(lis)*2
print(f'{inp[0]}{inp[1]*res}{inp[-1]}')