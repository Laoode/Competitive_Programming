inp = input()

x=inp.split()

has = [int(i) for i in x]

n,t,m=has

total = n*t*m
print(total)