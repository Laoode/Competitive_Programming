n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(input().strip())

star = []
for i in range(n):
    for j in range(m):
        if grid[i][j]=='*':
            star.append((i+1,j+1))

print(len(star))
for mine in star:
    print(mine[0],mine[1])