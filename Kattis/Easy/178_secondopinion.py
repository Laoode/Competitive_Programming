n=int(input())
h = n//3600
m = (n%3600)//60
d = (n%3600)%60
print(f'{h} : {m} : {d}')