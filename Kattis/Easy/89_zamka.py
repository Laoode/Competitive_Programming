def sum_of_digits(n):
    return sum(map(int, str(n)))

def find_min_x(a, b, s):
    for i in range(a, b + 1):
        if sum_of_digits(i) == s:
            return i
    return -1

def find_max_y(a, b, s):
    for i in range(b, a - 1, -1):
        if sum_of_digits(i) == s:
            return i
    return -1

def main():
    a = int(input().strip())
    b = int(input().strip())
    s = int(input().strip())
    
    min_x = find_min_x(a, b, s)
    max_y = find_max_y(a, b, s)
    
    print(min_x)
    print(max_y)

main()
