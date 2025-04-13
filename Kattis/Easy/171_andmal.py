inp = input()

a = inp*2
if len(a)>10:
    print(''.join(reversed(a[:9])))
elif len(a)==0:
    print("yudhy")
else:
    print(''.join(reversed(a)))