# -*- coding: utf8 -*-


import pytest


@pytest.mark.parametrize("x", [1,2,3])
@pytest.mark.parametrize("y", [8,3,7])
def test_foo(x, y):
    assert 1 + x - 1 == x
    assert 1 + x - 1 + y != x


def test_bar():
    pass
