v = input()

x=v.split()

x=[int(y) for y in x]

v,a,t = x

d = v*t + (0.5)*a*t**2
print(format(d,'.9f'))