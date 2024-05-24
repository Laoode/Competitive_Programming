x = int(input())
lis = []
for i in range(x):
    inp = input()
    inp =list(inp)
    a = inp[-1]
    a =int(a)
    inp.pop()
    c = ''.join(inp)
    c = int(c)
    total = c**a
    lis.append(total)

hasil = sum(lis)

print(hasil)