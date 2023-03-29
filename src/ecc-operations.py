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
    
    """
    def check(self) -> bool:
        return (4 * self.a**3 + 27 * self.b**2) % self.p != 0
    """

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
        if not p.check(self):
            raise ValueError("point p is not on curve")
        if not q.check(self):
            raise ValueError("point q is not on curve")
        if p == q:
            raise ValueError("can not add equal points -> use double function")
        if p.inf:
            return q
        elif q.inf:
            return p
        if p.is_inverted(p = q, ecc = self):
            return Point(0, 0, True)
        
        
        
        eeA = advancedEuklid(self.p, q.x - p.x)
        d = eeA[2] % self.p

        s = ((q.y - p.y) * d) % self.p
        x3 = ((s ** 2) - p.x - q.x) % self.p
        y3 = ((s * (p.x - x3)) - p.y) % self.p

        return Point(x3, y3)


    def check_Point(self, p: object) -> bool:
        pass
            

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
        return (self.x == obj.x) and (self.y == obj.y)


    def ord_Point(self, e: object) -> int:
        pass


    def check(self, e: object) -> bool: 
        return (self.y ** 2) % e.p == (self.x ** 3 + e.a * self.x + e.b) % e.p
    

    def is_inverted(self, p: object, ecc: object):
        temp = Point(self.x, -self.y)
        while temp.y < 0:
            temp.y += ecc.p
        return temp == p



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
    c = ECC(2, 2, 17)
    p = Point(5,1)
    q = Point(10,6)
    pq = c.add(p, q)
    print(pq)
