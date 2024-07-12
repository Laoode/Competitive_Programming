y = int(input())
z = 1000

if y >= 2021:
    for i in range(y - 2020):
        z += 100
    print(z)
else:
    print(z)