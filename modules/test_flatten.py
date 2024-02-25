#!/usr/bin/python
"""test_flatten.py - flattenList testing
"""
from .flatten import flattenList


def test_flatten_list():
    """test function of flattenList method"""

    result1 = flattenList([['1', 2, [3]], 4])
    result2 = flattenList(['1', 2, 3, [4], [], [[[[[[[[[5]]]]]]]]]])

    assert result1 == ['1', 2, 3, 4]
    assert result2 == ['1', 2, 3, 4, 5]



