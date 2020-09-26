import pytest


def test_len():
    s = ""
    assert len(s) == 0
    s = "abacd"
    assert len(s) == 5


@pytest.mark.parametrize("input_str,expected",
                         [("apple", "Apple"), ("aPPle", "Apple"), ("Apple", "Apple"), ("APPle", "Apple")])
def test_capitalize(input_str, expected):
    assert input_str.capitalize() == expected


def test_split():
    s = "ab"
    assert s.split() == ["ab"]
    s = "ab cde"
    assert s.split() == ["ab", "cde"]
    s = "appleandapricot"
    assert s.split("a") == ["", "pple", "nd", "pricot"]
    s = "fire ice and blood"
    assert s.split(' ', 1) == ["fire", "ice and blood"]


def test_adding():
    s1 = ""
    s2 = "abcd"
    assert s1 + s2 == "abcd"
    s3 = "ice"
    s4 = "fire"
    assert s3 + s4 == "icefire"
    assert s4 + s3 == "fireice"
    assert s2 + s3 + s4 == "abcdicefire"


class TestReplace:
    def test_replace(self):
        s = "applea"
        assert s.replace("a", "d") == "dppled"
        s = "apple"
        assert s.replace("c", "d") == "apple"
        s = "appleappstore"
        assert s.replace("app", "q") == "qleqstore"
        s = "apple appstore applied"
        assert s.replace("app", "q", 2) == "qle qstore applied"
