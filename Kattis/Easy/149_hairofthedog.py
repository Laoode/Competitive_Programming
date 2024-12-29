n = int(input())
list_days = []
for _ in range(n):
    days = input()
    list_days.append(days)

hungover=0
for i in range(len(list_days)):
    if list_days[i] == "drunk":
        if list_days[i+1] != "drunk":
            hungover+=1

print(hungover)