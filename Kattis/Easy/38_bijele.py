a, b, c, d, e, f = map(int, input().split())
n = []

def uji(z, expected):
    if z == expected:
        x = 0
    else:
        x = expected - z
    n.append(x)

uji(a, 1)
uji(b, 1)
uji(c, 2)
uji(d, 2)
uji(e, 2)
uji(f, 8)

hasil = ' '.join(map(str, n))
print(hasil)
