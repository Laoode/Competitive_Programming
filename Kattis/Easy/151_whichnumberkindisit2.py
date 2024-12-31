n = int(input())
list_t=[]
for _ in range(n):
    t = int(input())
    list_t.append(t)

def is_square(x):
    return x**.5 % 1 == 0
def is_odd(x):
    return x%2 == 1
    
for i in list_t:
    if is_square(i) & is_odd(i):
        print("OS")
    elif is_square(i):
        print("S")
    elif is_odd(i):
        print("O")
    else:
        print("EMPTY")
