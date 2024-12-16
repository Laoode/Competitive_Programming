a,b = map(int, input().split())
lis = []
los = []

for i in range (a):
 ing, res = map(int, input().split())
 formula = ing*(res/100)
 lis.append(formula)

for j in range (b):
 ing, res = map(int, input().split())
 formula = ing*(res/100)
 los.append(formula)

c = sum(lis)
d = sum(los)

if round(c) == round(d):
 print("same")
else:
 print("different")