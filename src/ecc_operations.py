import math
class ECC:
    def __init__(self, a: int, b: int, p: int):
        if not is_prime(p):
            raise ValueError("p is not a prime number")
        
        if (4 * a**3 + 27 * b**2) % p == 0:
            raise SyntaxError("parameters do not create a valid curve")
        
        self.a: int = a
        self.b: int = b
        self.p: int = p

    
    def __str__(self) -> str:
        return f"y**2 = x**3 + {self.a} * x + {self.b} mod {self.p}"
    

    def allPoints(self) -> list:
        arr = [Point(0, 0, True)]
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


    def ord_ECC(self) -> int:
        return len(self.allPoints())


    def double(self, p: object) -> object:
        if not isinstance(p, Point):
            raise TypeError("p is not of type Point")
        if not p.check(self):
            raise ValueError("point p is not on curve")

        if p.inf:
            return p

        eeA = advancedEuklid(self.p, 2 * p.y)
        d = eeA[2] % self.p

        s = ((3 * (p.x ** 2) + self.a) * d) % self.p

        x3 = ((s ** 2) - p.x - p.x) % self.p
        y3 = ((s * (p.x - x3)) - p.y) % self.p

        return Point(x3, y3, Point(x3, y3) == p)
     

    def add(self, p: object, q: object) -> object:
        if not isinstance(p, Point):
            raise TypeError("p is not of type Point")
        if not isinstance(q, Point):
            raise TypeError("q is not of type Point")
        if not p.check(self):
            raise ValueError(f"point p {p} is not on curve")
        if not q.check(self):
            raise ValueError(f"point q {q} is not on curve")
        if p == q:
            print(f"point p equals point q \n -> calling method double({p})")
            return self.double(p)
        
        if p.inf:
            return q
        elif q.inf:
            return p
        
        if p.get_inverted(self) == q:
            return Point(0, 0, True)

        eeA = advancedEuklid(self.p, q.x - p.x)
        d = eeA[2] % self.p

        s = ((q.y - p.y) * d) % self.p
        x3 = ((s ** 2) - p.x - q.x) % self.p
        y3 = ((s * (p.x - x3)) - p.y) % self.p

        return Point(x3, y3)
            

    def satz_v_hasse(self) -> tuple:
        low = (self.p + 1) - 2 * math.sqrt(self.p)
        high = (self.p + 1) + 2 * math.sqrt(self.p)
        return low, high

class Point:

    def __init__(self, x: int, y: int, inf = False):
        self.x = x
        self.y = y
        self.inf = inf


    def __str__(self) -> str:
        if self.inf:
            return "Infinte"
        else:
            return f"({self.x} | {self.y})"
    
    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Point):
            raise TypeError("obj is not of type Point")
        return (self.x == obj.x) and (self.y == obj.y)


    def ord_Point(self, ecc: ECC) -> int:
        if not self.check(ecc):
            raise ValueError(f"point is not on curve: {ecc}")

        tmp = self
        it = 1
        while not tmp.inf:
            if tmp == self:
                tmp = ecc.double(self)
            else:
                tmp = ecc.add(tmp, self)
            it += 1
        return it
            


    def check(self, ecc: ECC) -> bool:
        if self.inf:
            return self.inf
        else:
            return (self.y ** 2) % ecc.p == (self.x ** 3 + ecc.a * self.x + ecc.b) % ecc.p
    

    def get_inverted(self, ecc: ECC) -> object:
        if not self.check(ecc):
            raise ValueError(f"point is not on curve: {ecc}")
        if self.inf:
            return self

        if self.inf:
            return Point(0, 0, True)

        inv = Point(self.x, -self.y)
        while inv.y < 0:
            inv.y += ecc.p
        return inv
    
    def generate_subgroup(self, ecc: ECC) -> list:
        """generates subgroup of generator"""
        if not self.check(ecc):
            raise ValueError(f"point is not on curve: {ecc}")

        tmp = self
        ret = [self]
        while not tmp.inf:
            if tmp == self:
                tmp = ecc.double(self)
                ret.append(tmp)
            else:
                tmp = ecc.add(tmp, self)
                ret.append(tmp)
        return ret


def advancedEuklid(a: int, b: int) -> tuple:
    """erweiterter euklidischer Algorithmus zur Inversenberechnung"""
    if a == 0:
        return b, 0, 1
    eeA, x1, y1 = advancedEuklid(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return eeA, x, y

def is_prime(n: int) -> bool:
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

if __name__ == "__main__":
    c = ECC(2,2,17)
    p = Point(5, 1)
    print(c.satz_v_hasse())