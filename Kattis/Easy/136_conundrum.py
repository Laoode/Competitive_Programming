def split(s):
    return [s[i:i+3] for i in range(0,len(s), 3)]

inp = input()
result = split(inp)
reads = "Per "*len(result)
reads = reads.upper()
reads_re = reads.split()

count = 0
for i in range(len(result)):
    for j in range(3):
        if result[i][j] != reads_re[i][j]:
            count+=1
print(count)