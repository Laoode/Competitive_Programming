x1,y1,x2,y2 = map(float, input().split())

w = abs(x2-x1)
h = abs(y2-y1)

area = w*h
print(f'{area:.3f}')