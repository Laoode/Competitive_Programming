n,k = map(int,input().split())


c = list(map(int,input().split()))

b = len(c)-1
if c[0] == k:
    print("fyrst")
elif c [1] == k:
    print("naestfyrst")
else:
    for g in range(len(c)):
        if c[g] == k:
            print(f"{g+1} fyrst")
        else:
            None