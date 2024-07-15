l,r = map(int, input().split())


if l == 0 and r == 0:
    print('Not a moose') 
elif l == r:
    print('Even', l+r)
elif l != r:
    if l > r:
        print('Odd', l*2)
    else:
        print('Odd', r*2)