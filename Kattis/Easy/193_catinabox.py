h,w,l,c = map(int, input().split())
v = l * w * h

if c==v:
    print("COZY")
elif c<v:
    print("SO MUCH SPACE")
else:
    print("TOO TIGHT")