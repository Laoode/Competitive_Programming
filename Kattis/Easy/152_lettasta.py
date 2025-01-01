n = int(input())
m = int(input())

name = list(map(str, input().split()))

list_score=[]
for _ in range(m):
    score = list(map(int, input().split()))
    list_score.append(score)

total_scores=[0]*n
for i in range(m):
    for j in range(n):
        total_scores[j]+=list_score[i][j]
    
index = total_scores.index(max(total_scores))

print(name[index])