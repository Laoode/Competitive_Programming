count = int(input())
total_name=0
list_name=[]
while total_name < count:
    name=input()
    list_name.append(name)
    total_name+=1
for i in list_name:
    print(f'Takk {i}')