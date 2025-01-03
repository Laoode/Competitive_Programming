lis = []
for _ in range(5):
    contestant = list(map(int, input().split()))
    sum_con = sum(contestant)
    lis.append(sum_con)

print(f'{lis.index(max(lis))+1} {max(lis)}')