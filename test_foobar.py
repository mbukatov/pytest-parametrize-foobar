# -*- coding: utf8 -*-


import pytest


@pytest.mark.parametrize("x", [1,2,3])
@pytest.mark.parametrize("y", [8,3,7])
def test_foo(x, y):
    assert 1 + x - 1 == x
    assert 1 + x - 1 + y != x


@pytest.mark.parametrize("x", [1,2,3]) # positive
@pytest.mark.parametrize("y", [8,3,7]) # positive
@pytest.mark.parametrize("z", [None]) # negative
def test_bar(x, y, z):
    assert x is not None
    assert y is not None
    # assert z is not None
