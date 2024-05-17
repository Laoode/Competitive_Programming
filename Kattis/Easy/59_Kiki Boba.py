inp = input()

count_b = inp.count('b')
count_k = inp.count('k')

if count_b > count_k:
    print("boba")
elif count_k > count_b:
    print("kiki")
elif count_b == count_k and count_b != 0:
    print("boki")
else:
    print("none")
