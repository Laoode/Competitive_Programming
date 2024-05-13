while True:
    try:
        x,y = map(int, input().split())
        f = abs(x-y)  
        print(f)
    except EOFError:
        break