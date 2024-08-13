n = int(input())
x = 1
while True:
    rumus = x * (x+1) * (x+2)
    if rumus < n:
        x +=1
    else:
        break
print(x-1)