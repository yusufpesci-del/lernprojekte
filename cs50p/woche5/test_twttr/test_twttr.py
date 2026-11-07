from twttr import shorten


def test_lowercase():
    assert shorten("hello") == "hll"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_numbers():
    assert shorten("CS50") == "CS50"