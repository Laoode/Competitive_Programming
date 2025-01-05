while True:
    n = int(input())
    if n == -1:
        break
    list_nn=[]
    sampul=[]
    for _ in range(n):
        nn = list(map(int, input().split()))
        list_nn.append(nn)
    #Mencari Tetangga
    for i in list_nn:
        mine=[]
        for j in range(len(i)):
            if i[j]==1:
                mine.append(j)
        sampul.append(mine)
    #Memeriksa Segitiga
    weak_v=[]
    for i in range(n):
        is_weak=True
        for j in sampul[i]:
            for k in sampul[i]:
                if j!=k and list_nn[j][k]==1:
                    is_weak=False
                    break
            if not is_weak:
                break
        if is_weak:
            weak_v.append(i)
    print(" ".join(map(str, weak_v)))