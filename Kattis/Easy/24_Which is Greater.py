inp = input()

x=inp.split()

arr = [int(i) for i in x]

a,b = arr

if a>b:
    print(1)
else:
    print(0)