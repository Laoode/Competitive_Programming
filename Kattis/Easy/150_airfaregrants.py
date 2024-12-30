n = int(input())
flight = []
for _ in range(n):
    p = int(input())
    flight.append(p)
    
sponsor = max(flight)/2

pay = sponsor-min(flight)
pay =abs(pay) 

if sponsor>=min(flight):
    print(0)
else:
    print(int(pay))