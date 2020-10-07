import pytest


@pytest.fixture()
def new_list():
    yield [j for j in range(10)]


class TestIndexAssign:

    def test_positive_index(self, new_list):
        new_list[0] = -1
        new_list[3] = -1
        new_list[9] = -1
        expected_list = [-1, 1, 2, -1, 4, 5, 6, 7, 8, -1]
        assert new_list == expected_list
        with pytest.raises(IndexError):
            new_list[10]

    def test_negative_index(self, new_list):
        new_list[-1] = -1
        new_list[-3] = -1
        new_list[-10] = -1
        expected_list = [-1, 1, 2, 3, 4, 5, 6, -1, 8, -1]
        assert new_list == expected_list
        with pytest.raises(IndexError):
            new_list[-11]


def test_append(new_list):
    new_list.append(-1)
    expected_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
    assert expected_list == new_list


def test_count(new_list):
    assert new_list.count(2) == 1
    new_list.append(2)
    assert new_list.count(2) == 2

    assert new_list.count(-1) == 0
    new_list.append(-1)
    assert new_list.count(-1) == 1


@pytest.mark.parametrize("input_list,multiplier,expected",
                         [([1, 2, 3], 2, [1, 2, 3, 1, 2, 3]), ([1, 2], 0, []),
                          ([1, 2, 3, 4], 1, [1, 2, 3, 4])])
def test_multiply(input_list, multiplier, expected):
    assert input_list * multiplier == expected
