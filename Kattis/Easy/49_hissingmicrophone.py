inp = input()

for i in range(1, len(inp)):
    if inp[i] == 's' and inp[i-1] == 's':
        print("hiss")
        break
else:
    print("no hiss")