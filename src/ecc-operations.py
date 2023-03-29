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


    def double(self: object, p:object) -> object:
        pass


    def add(self: object, p: object, q: object) -> object:
        pass


    def check_Point(self: object, p: object) -> bool:
        pass
            

class Point:

    def __init__(self: object, x: int, y: int):
        self.x = x
        self.y = y


    def __str__(self: object) -> str:
        return f"({self.x} | {self.y})"
    
    def __eq__(self: object, obj: object) -> bool:
        if not isinstance(obj, Point):
            raise TypeError("Can only compare instances of circle")
        return (self.x == obj.x) and (self.y == obj.y)


    def ord_Point(self: object, e: object) -> int:
        pass


    def check(self: object, e: object) -> bool: 
        pass


ec = ECC(14, 5, 19)
t = ec.allPoints()
for i in t:
    print(i)


print(Point(1,1) == Point(1,1))