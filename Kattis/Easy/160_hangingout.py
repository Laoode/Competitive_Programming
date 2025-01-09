l, x = map(int, input().split())
group_not_allowed=0
total=0
for _ in range(x):
    m, p = map(str, input().split())
    p =  int(p)
    if m=='enter':
        p=p*1
    elif m=='leave':
        p=p*-1
    total+=p
    if total>l:
        group_not_allowed+=1
        total-=p
print(group_not_allowed)