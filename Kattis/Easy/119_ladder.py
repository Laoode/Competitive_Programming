def sin(x):
    pi = 3.141592653589793
    x = x % (2 * pi)
    
    # Menghitung deret Taylor untuk sin(x)
    term = x  
    sin_x = 0
    n = 1
    precision = 1e-10 
    
    while abs(term) > precision:
        sin_x += term
        term *= -x * x / (2 * n * (2 * n + 1))
        n += 1
    
    return sin_x

def bul(l):
    bulat = int(l)
    if l > bulat:
        return bulat+1
    return bulat
h, degrees = map(int, input().split())
radians = degrees * 3.141592653589793 / 180 
sin = sin(radians)
l = h/sin
print(bul(l))