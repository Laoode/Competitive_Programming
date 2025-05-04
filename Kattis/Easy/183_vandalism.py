name=['U', 'A', 'P', 'C']

a = input()

char_rem=''

for i in name:
    if i not in a:
        char_rem+=i
print(char_rem)