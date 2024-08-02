N = int(input())
N = bin(N)[2:]
rev = ''.join(reversed(N))
biner = int(rev,2)
print(biner)