class ECC:
    def __init__(self: object, a: int, b: int, p: int): # constructor
        self.a: int = a
        self.b: int = b
        self.p: int = p


    def __str__(self: object) -> str:   # toString method
        return f"y**2 = x**3 + {self.a} * x + {self.b} mod {self.p}"
    

    def check(self: object) -> bool:    # check if the elliptic curve is valid
        return not (4 * self.a**3 + 27 * self.b**2) % self.p == 0
    

    def allPoints(self: object) -> list:    # calculate all points on elliptic curve
        arr = [None]
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


    def ord_ECC(self: object) -> int:   # calculate rank of elliptic curve
        return len(self.allPoints(self))


    def double(self: object, p:object) -> object:   # doubles point p on elliptic curve
        pass


    def add(self: object, p: object, q: object) -> object:  # add point p to point q und elliptic curve
        pass


    def check_Point(self: object, p: object) -> bool:   # check if point p is on elliptic curve
        pass
            

class Point:

    def __init__(self: object, x: int, y: int): # constructor
        self.x = x
        self.y = y


    def __str__(self: object) -> str:   # toString method
        return f"({self.x} | {self.y})"


    def ord_Point(self: object, e: object) -> int:  # calculate rank on elliptic curve e
        pass


    def check(self: object, e: object) -> bool: # check if point is on elliptic curve e 
        pass


ec = ECC(2, 2, 17)
print(ec)
print(ec.check())
