n = int(input())

suhu = list(map(int, input().split()))  
avg_suhu = sum(suhu) // n 
print(avg_suhu)