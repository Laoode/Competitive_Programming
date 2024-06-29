n = int(input())
counts = {}
for i in range(n):
    a, b = input().split()
    b = int(b)
    if a in counts:
        counts[a] += b
    else:
        counts[a] = b
        
print(max(counts, key=counts.get))
