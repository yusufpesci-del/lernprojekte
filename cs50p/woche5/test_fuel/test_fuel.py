import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("cat/4")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(0) == "E"


def test_too_big():
    with pytest.raises(ValueError):
        convert("5/4")