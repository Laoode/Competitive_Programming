n, k = map(int, input().split())
lis = []
for _ in range(k):
    inp = int(input())
    lis.append(inp)
n_total = sum(lis)
n_less = n-k

        
minn = (n_total+n_less*-3)/n
maxx = (n_total+n_less*3)/n


print(f'{minn} {maxx}')