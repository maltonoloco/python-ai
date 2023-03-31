import sys, os
from src import ecc_operations as ECC
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_double():
    ecc = ECC.ECC(2, 2, 17)
    p = ECC.Point(5, 1)
    if ecc.double(p) == ECC.Point(6, 3):
        print("valid")
    else:
        print("not valid")

    p = ECC.Point(6, 3)
    if ecc.double(p) == ECC.Point(3, 1):
        print("valid")
    else:
        print("not valid")
    
    p = ECC.Point(3, 1)
    if ecc.double(p) == ECC.Point(13, 7):
        print("valid")
    else:
        print("not valid")


def test_add():
    ecc = ECC.ECC(2, 2, 17)
    p = ECC.Point(5, 1)
    q = ECC.Point(6, 3)
    if ecc.add(p, q) == ECC.Point(10, 6):
        print("valid")
    else:
        print("not valid")
    
    q = ECC.Point(9, 16)
    if ecc.add(p, q) == ECC.Point(16, 13):
        print("valid")
    else:
        print("not valid")
    
    q = ECC.Point(5, 16)

    if ecc.add(p, q) == ECC.Point(0, 0, True):
        print("valid")
    else:
        print("not valid")

def test_ord_ECC():
    ecc = ECC.ECC(2, 2, 17)
    if ecc.ord_ECC() == 19:
        print("valid")
    else:
        print("not valid")
    

def test_ord_Point():
    ecc = ECC.ECC(2, 2, 17)
    p = ECC.Point(5, 1)
    if p.ord_Point(ecc) == 19:
        print("valid")
    else:
        print("not valid")

def test_point_check():
    ecc = ECC.ECC(2, 2, 17)
    p = ECC.Point(5, 1)
    if p.check(ecc):
        print("valid")
    else:
        print("not valid")
    
    p = ECC.Point(3, 2)
    if not p.check(ecc):
        print("valid")
    else:
        print("not valid")
    
    p = ECC.Point(0, 0, True)
    if p.check(ecc):
        print("valid")
    else:
        print("not valid")
    

def test_get_inverted():
    ecc = ECC.ECC(2, 2, 17)
    p = ECC.Point(5, 1)
    if p.get_inverted(ecc) == ECC.Point(5, 16):
        print("valid")
    else:
        print("not valid")
    
    p = ECC.Point(16, 13)
    if p.get_inverted(ecc) == ECC.Point(16, 4):
        print("valid")
    else:
        print("not valid")
    
    p = ECC.Point(0, 0, True)
    if p.get_inverted(ecc) == ECC.Point(0, 0, True):
        print("valid")
    else:
        print("not valid")