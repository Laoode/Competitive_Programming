r,c,zr,zc = map(int, input().split())
lis = []
for _ in range(r):
    inp = list(map(str, input()))
    mat_lis=[]
    for j in range(c):
        m = inp[j]*zc
        mat_lis.append(m)
    for i in range(zr):
        lis.append(mat_lis)
    
for k in lis:
    print(''.join(map(str, k)))