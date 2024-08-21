n = input()
camp = ''
i =1
while len(camp)<len(n):
    camp += str(i)
    i+=1

if camp == n:
    print(camp[-1])
else:
    print(-1)