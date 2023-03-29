class ECC:
    def __init__(self: object, a: int, b: int, p: int):
        self.a: int = a
        self.b: int = b
        self.p: int = p

    

    def __str__(self: object) -> str:
        return f"y**2 = x**3 + {self.a} * x + {self.b} mod {self.p}"
    

    def check(self: object) -> bool:
        return not (4 * self.a**3 + 27 * self.b**2) % self.p == 0
    

    def allPoints(self: object) -> list:
        arr = []
        tab1 = []
        tab2 = []
        for i in range(self.p):
            tab1.append((i, i**2 % self.p))
            tab2.append((i, (i**3 + self.a * i + self.b) % self.p))
        for i in tab2:
            for q in range(2):
                for j in tab1:
                    if i[1] == j[1] and (Point(i[0], j[0])) not in arr:
                        arr.append(Point(i[0], j[0]))
        return arr


    def ord_ECC(self: object) -> int:
        return len(self.allPoints(self))


    def double(self: object, p: object) -> object:
        if not isinstance(p, Point):
            raise TypeError("p is not of Type Point")
        
        eeA = advancedEuklid(p, 2 * p.y)
        d = eeA[2] % self.p

        s = ((3 * (p.x ** 2) + self.a) * d) % self.p

        x3 = ((s ** 2) - p.x - p.x) % self.p
        y3 = ((s * (p.x - x3)) - p.y) % self.p

        return Point(x3, y3, Point(x3, y3) == p)
        





    def add(self: object, p: object, q: object) -> object:
        pass


    def check_Point(self: object, p: object) -> bool:
        pass
            

class Point:

    def __init__(self: object, x: int, y: int, inf = False):
        self.x = x
        self.y = y
        self.inf = inf


    def __str__(self: object) -> str:
        return f"({self.x} | {self.y})"
    
    def __eq__(self: object, obj: object) -> bool:
        if not isinstance(obj, Point):
            raise TypeError("Can only compare instances of points")
        return (self.x == obj.x) and (self.y == obj.y)


    def ord_Point(self: object, e: object) -> int:
        pass


    def check(self: object, e: object) -> bool: 
        pass


def advancedEuklid(a: int, b: int) -> tuple:
    """erweiterter euklidischer Algorithmus zur Inversenberechnung"""
    if a == 0:
        return b, 0, 1
    eeA, x1, y1 = advancedEuklid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return eeA, x, y

ec = ECC(12, 4, 23)
ec.double()
