# -*- coding: utf8 -*-

import pytest


@pytest.fixture(params=[1,"foo", None])
def single_one(request):
    return [request.param]
