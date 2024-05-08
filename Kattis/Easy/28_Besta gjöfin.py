line = int(input())
lis = []
y=[]
for i in range(line):
    inp = input()
    x = inp.split()
    lis.append(x)
for i in lis:
    for j in i:
        y.append(j)

angk = []
hur = []
for i in range(1,len(y),2):
    angk.append(y[i])
for i in range(0,len(y),2):
    hur.append(y[i])
jadi = list(map(int,angk))

max_v = max(jadi)
for i in range(len(jadi)):
    if jadi[i] == max_v:
        print(hur[i])
    else:
        None

