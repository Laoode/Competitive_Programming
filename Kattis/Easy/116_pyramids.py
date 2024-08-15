n = int(input())

h=0
total_block=0
while True:
    h+=1
    sisi = (2*h-1)**2
    if total_block+sisi>n:
        break
    total_block+=sisi
print(h-1)