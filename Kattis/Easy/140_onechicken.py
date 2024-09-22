p, c = map(int, input().split())

if c > p:
    pieces_left = c - p
    print(f"Dr. Chaz will have {pieces_left} piece{'s' if pieces_left > 1 else ''} of chicken left over!")
else:
    pieces_needed = p - c
    print(f"Dr. Chaz needs {pieces_needed} more piece{'s' if pieces_needed > 1 else ''} of chicken!")
