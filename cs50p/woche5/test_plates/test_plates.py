from plates import is_valid


def test_length():
    assert is_valid("AA")
    assert is_valid("AAAAAA")
    assert not is_valid("H")
    assert not is_valid("OUTATIME")


def test_two_letters():
    assert is_valid("CS50")
    assert not is_valid("50")
    assert not is_valid("1A")


def test_digits_at_end():
    assert is_valid("AAA22")
    assert is_valid("NRVOUS")
    assert not is_valid("CS50P")
    assert not is_valid("H3LLO")


def test_no_leading_zero():
    assert is_valid("CS50")
    assert not is_valid("CS05")


def test_nopunctuation():
    assert is_valid("CS50")
    assert not is_valid("PI3-14")
    assert not is_valid("PI3.14")
    assert not is_valid("CS 50")
    assert not is_valid("CS50!")