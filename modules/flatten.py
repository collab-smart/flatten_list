#!/usr/bin/python
"""flatten.py - extended utils
"""


def flattenList(nestedList):
    """flatten a nested list using a recursive approach"""
    if not nestedList:  # if nestedlist is empty
        return []
    if isinstance(nestedList[0], list):  # if the first element is a list
        return flattenList(nestedList[0]) + flattenList(nestedList[1:])  # recursively call the function
    return nestedList[:1] + flattenList(nestedList[1:])  # recursively call the function
