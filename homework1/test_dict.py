import pytest


def test_keys_addressing():
    dict1 = {"a": 1, "b": 2, "c": 3}
    assert dict1["a"] == 1
    assert dict1["c"] == 3
    with pytest.raises(KeyError):
        assert dict1["d"]
    dict1["a"] = -1
    assert dict1 == {"a": -1, "b": 2, "c": 3}
    dict2 = {"a": 1, "b": 2}
    dict2["c"] = 3
    assert dict2 == {"a": 1, "b": 2, "c": 3}


@pytest.mark.parametrize("input_dict,expected",
                         [({}, []), ({"abcd": 22, "tera": 31, "kilo": 52}, ["abcd", "tera", "kilo"]),
                          ({"dfer": 2}, ["dfer"])])
def test_keys(input_dict, expected):
    assert list(input_dict.keys()) == expected


@pytest.mark.parametrize("input_dict,expected",
                         [({}, []), ({"a": 2}, [2]), ({"abcd": 2, "gera": 3, "ture": 4}, [2, 3, 4])])
def test_values(input_dict, expected):
    assert list(input_dict.values()) == expected


def test_clear():
    dict1 = {}
    dict1.clear()
    assert dict1 == {}
    dict2 = {"asdf": 23}
    dict2.clear()
    assert dict2 == {}
    dict3 = {"jit": 12, "kyr": 22, "fgaf": 14}
    dict3.clear()
    assert dict3 == {}


class TestPop:
    def test_popitem(self):
        dict1 = {}
        with pytest.raises(KeyError):
            dict1.popitem()
        dict2 = {"abcd": 1}
        assert dict2.popitem() == ("abcd", 1)
        assert dict2 == {}
        dict3 = {"abcd": 1, "treat": 2, "geta": 4}
        assert dict3.popitem() == ("geta", 4)
