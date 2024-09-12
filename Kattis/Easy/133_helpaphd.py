n = int(input())
lis=[]
for _ in range(n):
    inp = input()
    if 'P=NP'==inp:
        lis.append('skipped')
    elif '+' in inp:
        a, b = map(int, inp.split('+'))
        lis.append(a + b)

for j in lis:
    print(j)

        
        