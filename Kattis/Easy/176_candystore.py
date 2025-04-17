name, aka = map(int, input().split())
lis_name={}
lis_aka=[]
for _ in range(name):
    add=""
    inp = list(map(str, input().split()))
    for i in inp:
        add=add+i[0]
    real_name=' '.join(map(str, inp))
    lis_name[real_name]=add
    
for _ in range(aka):
    inp = input()
    lis_aka.append(inp)

seen=set()
dup=set()
for i in lis_name.values():
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)
        
for j in lis_aka:
    if j in dup:
        print("ambiguous")
    elif j in lis_name.values():
        for key,value in lis_name.items():
            if value==j:
                print(key)
    else:
        print("nobody")