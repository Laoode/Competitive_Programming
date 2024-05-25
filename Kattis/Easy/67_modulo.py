los = []
for i in range(10):
    inp = int(input())
    a = inp%42
    los.append(a)

les = []
for i in los:
    if i not in les:
        les.append(i)
    else:
        None
print(len(les))