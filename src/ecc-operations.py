def erweiterterEuklid(a, b):
    """erweiterter euklidischer Algorithmus zur Inversenberechnung"""
    if a == 0:
        return b, 0, 1
    eeA, x1, y1 = erweiterterEuklid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return eeA, x, y


def check(a, b, p, g):  # ell. Kurve der Form y^2 = x^3 + a*x + b mod p. Punkte g und h als Tupel (x, y)
    """ueberprueft ob ein Punkt g auf der ell. Kurve liegt"""
    if g is None:
        return True

    if (g[1] ** 2) % p == (g[0] ** 3 + a * g[0] + b) % p:
        return True
    else:
        return False


def punktaddition(a, b, p, g, h):  # ell. Kurve der Form y^2 = x^3 + a*x + b mod p. Punkte g und h als Tupel (x, y)
    if g is None and h is not None:
        return h
    elif h is None and g is not None:
        return g
    elif h is None and g is None:
        return

    if g == h:
        raise SyntaxError("Punkte muessen verschieden sein")
    temp = erweiterterEuklid(p, h[0] - g[0])
    d = temp[2] % p

    s = ((h[1] - g[1]) * d) % p
    #print("s: " + str(s))

    x3 = (s ** 2 - g[0] - h[0]) % p
    y3 = (s * (g[0] - x3) - g[1]) % p

    if check(a, b, p, (x3, y3)):
        return x3, y3
    else:
        return  # der Punkt im unendlichen ist None


def punktverdopplung(a, b, p, g):  # ell. Kurve der Form y^2 = x^3 + a*x + b mod p. Punkte g und h als Tupel (x, y)
    if g is None:
        return  # der Punkt im unendlichen ist None

    temp = erweiterterEuklid(p, 2 * g[1])
    d = temp[2] % p

    s = ((3 * (g[0] ** 2) + a) * d) % p
    #print("s: " + str(s))

    x3 = ((s ** 2) - g[0] - g[0]) % p
    y3 = ((s * (g[0] - x3)) - g[1]) % p

    if check(a, b, p, (x3, y3)):
        return x3, y3
    else:
        return  # der Punkt im unendlichen ist Noney


#print(punktverdopplung(5, 4, 7, (5,0)))
#print(punktaddition(5, 4, 7, (3,2), (2, 6)))

# (3,2)

#print(check(5, 4, 7, (5,0)))

def ord(a, b, m, p):
    q = p
    i = 2
    while q != None:
        if p == q:
            q = punktverdopplung(a, b, m, p)
        else:
            q = punktaddition(a, b, m, p, q)
        print(str(i) + ". " + str(q))
        i += 1

def allePunkte(a, b, p):
    arr = [None]
    tab1 = []
    tab2 = []
    for i in range(p):
        tab1.append((i, (i*i) % p))  #y
        tab2.append((i, (i*i*i + a * i + b) % p))   #x
    for i in tab2:
        for q in range(2):
            for j in tab1:
                if i[1] == j[1] and (i[0], j[0]) not in arr:
                    arr.append((i[0], j[0]))

    return arr


ord(5, 4, 7, (3,2))
