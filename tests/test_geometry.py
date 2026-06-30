from atlas.core.gemoetry import Rect


def test_area():

    r = Rect(0,0,100,100)

    assert r.area == 10000

def test_contains():

    a = Rect(0,0,100,100)

    b = Rect(10,10,20,20)

    assert a.contains(b)