n = int(input())
lis = []
for i in range(n):
    inp = input()
    lis.append(inp)
if len(lis) > 1:
    print("blandad best")
else:
    print(lis[0])