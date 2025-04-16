lis=[]
for _ in range(5):
    inp=input()
    if "FBI" in inp:
        lis.append(_+1)
    
if lis:
    print(' '.join(map(str, lis)))
else:
    print("HE GOT AWAY!")