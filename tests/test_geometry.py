from atlas.core.geometry import Rect


def test_area():

    r = Rect(0, 0, 100, 100)

    assert r.area == 10000


def test_contains():

    a = Rect(0, 0, 100, 100)
    b = Rect(10, 10, 20, 20)
    assert a.contains(b)


def test_iou():
    a = Rect(x0=0, y0=0, x1=10, y1=10)
    b = Rect(x0=5, y0=5, x1=15, y1=15)
    assert round(a.iou(b), 3) > 0
