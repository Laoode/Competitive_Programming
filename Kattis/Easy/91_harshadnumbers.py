a = int(input())

while True:
    a_str = str(a)
    digit_sum = 0 
    for digit in a_str:
        digit_int = int(digit)
        digit_sum += digit_int
    
    if a % digit_sum == 0:
        break
    a += 1

print(a)