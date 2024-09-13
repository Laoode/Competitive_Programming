n = int(input())
pop = list(map(int, input().split()))

pop.sort()
setengah = n // 2 + 1

hasil = 0
for i in range(n):
    if i < setengah:
        a = pop[i] // 2
        hasil += a
    else:
        hasil += pop[i]

print(hasil)