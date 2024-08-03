t, b, i = map(int, input().split())
total_h = b+i
c = 0
for _ in range(t):
    a = int(input())
    if a + 14 <= total_h:
        c+=1
print(c)
