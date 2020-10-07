import pytest


def test_add():
    set1 = set()
    set1.add(1)
    assert set1 == {1}
    set2 = {1, 2, 3, 4}
    set2.add(5)
    assert set2 == {1, 2, 3, 4, 5}
    set3 = {1, 2, 3, 4}
    set3.add(1)
    assert set3 == {1, 2, 3, 4}


def test_len():
    set1 = set()
    assert len(set1) == 0
    set2 = {1, 2, 3}
    assert len(set2) == 3
    set3 = {1, 1, 2, 3, 2}
    assert len(set3) == 3


def test_remove():
    set1 = {1, 2, 3, 4}
    set1.remove(3)
    assert set1 == {1, 2, 4}
    set2 = {1, 2, 3, 4, 1, 2}
    set2.remove(2)
    assert set2 == {1, 3, 4}
    set3 = {1, 2, 3, 4}
    with pytest.raises(KeyError):
        set3.remove(5)


class TestJoinMethods:
    @pytest.mark.parametrize("input_set1,input_set2,expected_set",
                             [({1, 2, 3, 4, 4}, set(), set()), ({1, 2, 3, 4, 5, 6}, {1, 5, 6}, {1, 5, 6}),
                              ({1, 2, 3, 4, 5}, {2, 3, 7, 8}, {2, 3}), ({2, 6, 8}, {1, 3, 4, 5}, set())])
    def test_intersection(self, input_set1, input_set2, expected_set):
        assert input_set1.intersection(input_set2) == expected_set

    @pytest.mark.parametrize("input_set1,input_set2,expected_set",
                             [(set(), {1, 2, 3}, {1, 2, 3}), ({1, 2, 3, 4, 5}, {1, 2, 3}, {1, 2, 3, 4, 5}),
                              ({1, 2, 3, 4, 5}, {2, 3, 4, 7, 8}, {1, 2, 3, 4, 5, 7, 8}),
                              ({1, 2, 3}, {4, 5, 6}, {1, 2, 3, 4, 5, 6})])
    def test_union(self, input_set1, input_set2, expected_set):
        assert input_set1.union(input_set2) == expected_set
