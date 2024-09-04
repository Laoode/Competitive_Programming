n = int(input())
m = int(input())

jumlah_tim = m//n
sisa = m%n
for i in range(n):
    if i < sisa:
        print('*'*(jumlah_tim+1))
    else:
        print('*'*jumlah_tim)