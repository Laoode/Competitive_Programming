inp = int(input())
lis=[]
for i in range(inp):
    qaly = input()
    a = qaly.split()
    b = [float(c) for c in a]
    x,y = b
    f = x*y
    lis.append(f)

total=sum(lis)
angka="{:.3f}".format(total)
print(angka)