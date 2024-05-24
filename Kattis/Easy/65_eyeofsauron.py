x= input()
lis = list(x)
y = len(lis)
z = y/2 -1
z = int(z)
if y%2 ==0:
    if lis[z] == '(' and lis[z+1] ==')':
        print("correct")
    else:
        print("fix")
else:
    print("fix")