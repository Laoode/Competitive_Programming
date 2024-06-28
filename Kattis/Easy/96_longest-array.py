arr = list(map(int, input().split()))
longest_streak = 1
current_streak = 1
for i in range(1, len(arr)):
    if arr[i] == arr[i - 1] + 1:
        current_streak += 1
    else:
        longest_streak = max(longest_streak, current_streak)
        current_streak = 1
print(max(longest_streak, current_streak))