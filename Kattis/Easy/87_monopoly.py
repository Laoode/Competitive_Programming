def probabilitas(hotel):
    combinasi = [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    valid = 0
    for i in hotel:
        valid+=combinasi[i]
    probablity = valid/36
    return probablity

n = int(input())
lis = list(map(int, input().split()))

hotel = probabilitas(lis)

print(hotel)