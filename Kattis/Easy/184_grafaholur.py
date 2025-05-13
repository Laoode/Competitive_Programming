n = int(input())
h = int(input())
x = int(input())
m = int(input())
y = int(input())

#1 pekerja
total_xh = x/(n*h) #meter/jam

# m pekerja
mh = m*total_xh #meter/jam

# total
total_h = y/mh

print("{:.15f}".format(total_h))