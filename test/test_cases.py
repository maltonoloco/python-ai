import sys, os
from src import ecc_operations as ECC
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_valid_elliptic_curve():
    ec = ECC.ECC(2, 2, 17)
    with pytest.raises(ValueError):
        ec2 = ECC.ECC(2, 2, 18)
    with pytest.raises(ValueError):
        ec3 = ECC.ECC(5, 16, 17)
    


def test_add():
    ecc = ECC.ECC(2, 2, 17)
    p = ECC.Point(5, 1)
    q = ECC.Point(6, 3)
    assert(ecc.add(p, q) == ECC.Point(10, 6))
    q = ECC.Point(5, 16)
    assert(ecc.add(p, q) == ECC.Point(0, 0, True))
    q = ECC.Point(5, 2)
    with pytest.raises(ValueError):
        ecc.add(p, q)
    

def test_ord_Point():
    ecc = ECC.ECC(2, 2, 17)
    p = ECC.Point(5, 1)
    assert(p.ord_Point(ecc) == 19)

    p = ECC.Point(16, 14)
    with pytest.raises(ValueError):
        p.ord_Point(ecc)

def test_point_check():
    ecc = ECC.ECC(2, 2, 17)

    p = ECC.Point(5, 1)
    assert(p.check(ecc))

    p = ECC.Point(3, 2)
    assert(not p.check(ecc))

    p = ECC.Point(0, 0, True)
    assert(p.check(ecc))

def test_get_inverted():
    ecc = ECC.ECC(2, 2, 17)

    p = ECC.Point(5, 1)
    assert(p.get_inverted(ecc) == ECC.Point(5, 16))
    
    p = ECC.Point(16, 13)
    assert(p.get_inverted(ecc) == ECC.Point(16, 4))
    
    p = ECC.Point(16, 14)
    with pytest.raises(ValueError):
        p.get_inverted(ecc)

    p = ECC.Point(0, 0, True)
    assert(p.get_inverted(ecc) == ECC.Point(0, 0, True))

def test_double():
    ecc = ECC.ECC(2, 2, 17)
    
    p = ECC.Point(5, 1)
    assert(ecc.double(p) == ECC.Point(6, 3))

    p = ECC.Point(16, 14)
    with pytest.raises(ValueError):
        ecc.double(p)

    p = ECC.Point(0, 0, True)
    assert(ecc.double(p) == ECC.Point(1, 1, True))
