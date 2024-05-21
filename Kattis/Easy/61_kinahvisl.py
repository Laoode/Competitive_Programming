inp1 = input()
inp2 = input()
los = []

a = len(inp1)
for i in range(a):
    if inp1[i] != inp2[i]:
        los.append(1)
    else:
        None


print(sum(los) + 1)