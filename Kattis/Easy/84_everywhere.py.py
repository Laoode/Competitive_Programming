n = int(input())

los = []
for h in range(n):
    i = int(input())
    lis = []
    if h!=n:
        for j in range(i):
            inp = input()
            if inp not in lis:
                lis.append(inp)
        a = len(lis)
        los.append(a)
for g in los:
    print(g)