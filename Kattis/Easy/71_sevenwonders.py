inp = input()
t=0
c=0
g=0

for j in inp:
    if j == 'T':
        t+=1
    elif j == 'C':
        c+=1
    elif j == 'G':
        g+=1
total = t*2+c2+g*2
score = min(t,c,g)

print(total+score*7)