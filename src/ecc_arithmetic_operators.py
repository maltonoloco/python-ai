from __future__ import annotations

class ECC:
    def __init__(self, a: int, b: int, p: int):
        if not is_prime(p):
            raise ValueError("p is not a prime number")
        
        if (4 * a**3 + 27 * b**2) % p == 0:
            raise SyntaxError("parameters do not create a valid curve")
        
        self.a: int = a
        self.b: int = b
        self.p: int = p

    def __eq__(self, ecc: ECC) -> bool:
        return self.a == ecc.a and self.b == ecc.b and self.p == ecc.p

    def __str__(self) -> str:
        return f"y**2 = x**3 + {self.a} * x + {self.b} mod {self.p}"

    def double(self, p: Point) -> Point:
        if not p.check(self):
            raise ValueError(f"point p {p}is not on curve")
        
        if p.inf:
            return p

        eeA = advancedEuklid(self.p, 2 * p.y)
        d = eeA[2] % self.p

        s = ((3 * (p.x ** 2) + self.a) * d) % self.p

        x3 = ((s ** 2) - p.x - p.x) % self.p
        y3 = ((s * (p.x - x3)) - p.y) % self.p

        return Point(x3, y3, self, Point(x3, y3, self) == p)
     

    def add(self, p: Point, q: Point) -> Point:
        if not p.check(self):
            raise ValueError(f"point p {p} is not on curve")
        if not q.check(self):
            raise ValueError(f"point q {q} is not on curve")
        if p == q:
            return self.double(p)
        
        if p.inf:
            return q
        elif q.inf:
            return p
        
        if p.get_inverted(self) == q:
            return Point(0, 0, self,  True)

        eeA = advancedEuklid(self.p, q.x - p.x)
        d = eeA[2] % self.p

        s = ((q.y - p.y) * d) % self.p
        x3 = ((s ** 2) - p.x - q.x) % self.p
        y3 = ((s * (p.x - x3)) - p.y) % self.p

        return Point(x3, y3, self)

class Point(ECC):
    def __init__(self, x: int, y: int, ecc: ECC, inf = False):
        if logical_xor(((y ** 2) % ecc.p != (x ** 3 + ecc.a * x + ecc.b) % ecc.p), inf):
        #if (((y ** 2) % ecc.p != (x ** 3 + ecc.a * x + ecc.b) % ecc.p) and not inf) or (not ((y ** 2) % ecc.p != (x ** 3 + ecc.a * x + ecc.b) % ecc.p)) and inf:
            raise ValueError("point is not on curve")
        ECC.__init__(self, ecc.a, ecc.b, ecc.p)
        self.x = x
        self.y = y
        self.inf = inf

    def __str__(self) -> str:
        if self.inf:
            return "Infinte"
        else:
            return f"({self.x} | {self.y})"

    def get_super(self):
        return ECC(self.a, self.b, self.p)
    
    def __eq__(self, obj: Point) -> bool:
        return (self.x == obj.x) and (self.y == obj.y) and (self.get_super() == obj.get_super())

    def __add__(self, obj: Point) -> Point:
        if self.get_super() != obj.get_super():
            raise ValueError("points are not on the same curve")

        ecc = self.get_super()
        return ecc.add(self, obj)

    def __mul__(self, ctr: int) -> Point:
        if ctr < 1:
            raise ValueError("cant multiply with int < 1")
        res = self
        for i in range(ctr - 1):
            res = res + self
        return res

    def get_inverted(self, ecc: ECC) -> Point:
        if self.inf:
            return self

        inv = Point(self.x, -self.y, ECC(self.a, self.b, self.p))
        while inv.y < 0:
            inv.y += ecc.p
        return inv


        
        
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

def logical_xor(b1: bool, b2: bool) -> bool:
    return (b1 and not b2) or (not b1 and b2)

if __name__ == "__main__":
    ec1 = ECC(2, 2, 17)
    ec2 = ECC(3, 2, 17)
    p1 = Point(5, 1, ec1)
    p2 = Point(6, 3, ec1)
    for i in range(19):
        print(f"{i+1}:   {p1 * (i+1)}")