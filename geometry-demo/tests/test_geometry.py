import pytest
from geometry import shapes, utils

def test_square_area_zero_and_positive():
    assert shapes.Square(0).area() == 0
    assert shapes.Square(2).area() == pytest.approx(4.0)
    assert shapes.Square(3.5).area() == pytest.approx(12.25)

def test_circle_area_zero_and_positive():
    assert shapes.Circle(0).area() == 0
    assert shapes.Circle(1).area() == pytest.approx(3.14159, 1e-2)
    assert shapes.Circle(2.5).area() == pytest.approx(19.63495, 1e-2)

def test_stats_keys_and_values():
    s = shapes.Square(2)
    c = shapes.Circle(1)
    stats = utils.area_stats(s, c)

    assert isinstance(stats, dict)
    assert set(stats.keys()) == {"n", "total", "mean", "min", "max"}
    assert stats["n"] == 2
    assert stats["total"] == pytest.approx(s.area() + c.area())
    assert stats["mean"] == pytest.approx((s.area() + c.area()) / 2)
    assert stats["min"] == pytest.approx(min(s.area(), c.area()))
    assert stats["max"] == pytest.approx(max(s.area(), c.area()))
    

def test_stats_raises_without_shapes():
    with pytest.raises(ValueError):
        utils.area_stats()
