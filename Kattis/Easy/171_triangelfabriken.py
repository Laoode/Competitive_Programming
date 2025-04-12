a=int(input())
b=int(input())
c=int(input())

lis=[a,b,c]
cek=[]
for i in lis:
    if i >90:
        print("Trubbig Triangel")
        cek.append(i)
        break
    if i==90:
        print("Ratvinklig Triangel")
        cek.append(i)
        break

if not cek:
    print("Spetsig Triangel")