n = int(input())
total=0
for _ in range(n):
    name=input()
    kronor = int(input())
    total+=kronor
    
if total > 0:
    print("Usch, vinst")
elif total < 0:
    print("Nekad")
else:
    print("Lagom")