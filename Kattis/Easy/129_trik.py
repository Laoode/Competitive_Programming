inp = input()
inp = inp.upper()
glass = 1

for i in range(len(inp)):
    if inp[i] == 'A':
        if glass == 1:
            glass = 2
        elif glass == 2:
            glass = 1
    elif inp[i] == 'B':
        if glass == 2:
            glass = 3
        elif glass == 3:
            glass = 2
    elif inp[i] == 'C':
        if glass == 1:
            glass = 3
        elif glass == 3:
            glass = 1

print(glass)
