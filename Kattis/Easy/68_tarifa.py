x = int(input())
n = int(input())
arr = []
for i in range(n):
    inp = int(input())
    arr.append(inp)
arr = sum(arr)  

sisa = x*n - arr

total = sisa+x
print(total)