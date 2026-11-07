from bank import value


def test_lowercase():
    assert value("hello") == 0


def test_uppercase():
    assert value("Hello") == 0

def test_uppercase_2():
    assert value("HELLO") == 0

def test_startswith_h():
    assert value("hi") == 20
    assert value("How are you") == 20
    assert value("hey") == 20

def test_any():
    assert value("What's up") == 100
    assert value("good morning") == 100
