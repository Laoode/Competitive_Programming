inp = input()
inp = inp.lower()
lis = []

for j in range(len(inp)):
    if j == len(inp) - 1:
        lis.append(inp[j])
    else:
        if inp[j] != inp[j + 1]:
            lis.append(inp[j])

print("".join(lis))
