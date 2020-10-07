import pytest


class TestArithmetic:
    @pytest.mark.parametrize("int1,int2,expected",
                             [(10, 15, 25), (0, 5, 5), (0, -5, -5), (3, -2, 1), (-5, -10, -15)])
    def test_adding(self, int1, int2, expected):
        assert int1 + int2 == expected

    @pytest.mark.parametrize("int1,int2,expected",
                             [(0, 5, 0), (0, -5, 0), (1, 2, 2), (1, -2, -2), (3, 4, 12),
                              (-3, 4, -12), (-3, -4, 12)])
    def test_multiplying(self, int1, int2, expected):
        assert int1 * int2 == expected

    @pytest.mark.parametrize("int1,int2,expected",
                             [(0, 5, 0), (5, 1, 5), (4, 4, 1.0), (-4, -2, 2.0), (4, 2, 2.0), (-4, 2, -2.0),
                              (4, 3, 1.3333333333333333), (-17, 13, -1.3076923076923077)])
    def test_division(self, int1, int2, expected):
        assert int1 / int2 == expected

    @pytest.mark.parametrize("int1,int2,expected",
                             [(0, 5, 0), (7, 1, 7), (6, 6, 1), (4, 2, 2), (-4, 2, -2), (4, -2, -2), (-4, -2, 2),
                              (4, 3, 1), (-4, 3, -2)])
    def test_integer_division(self, int1, int2, expected):
        assert int1 // int2 == expected

    @pytest.mark.parametrize("int1,int2,expected",
                             [(0, 10, 0), (10, 1, 0), (10, 10, 0), (6, 3, 0), (-6, 3, 0), (5, 3, 2), (-5, 3, 1)])
    def test_remainder(self, int1, int2, expected):
        assert int1 % int2 == expected

    @pytest.mark.parametrize("int1", [-1, 0, 1])
    def test_zero_division(self, int1):
        with pytest.raises(ZeroDivisionError):
            int1 / 0
        with pytest.raises(ZeroDivisionError):
            int1 // 0
        with pytest.raises(ZeroDivisionError):
            int1 % 0
