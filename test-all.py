#!/usr/bin/python
"""test-all.py - main testing file
"""
from modules.flatten import flattenList
from tracker import TempTracker


def runFlatten():
    """run flattening."""
    # Examples:

    # >> > flattenList([['1', 2, [3]], 4])
    # ['1', 2, 3, 4]
    result1 = flattenList([['1', 2, [3]], 4])
    print(result1)

    # >> > flattenList(['1', 2, 3, [4], [], [[[[[[[[[5]]]]]]]]]])
    # ['1', 2, 3, 4, 5]
    result2 = flattenList(['1', 2, 3, [4], [], [[[[[[[[[5]]]]]]]]]])
    print(result2)


def runTrackers():
    """run trackers."""
    # Examples:

    # >> > temperatures = [22, 7, 22, 13, 2, 31, 18]
    # >> > tracker = TempTracker()
    # >> > tracker.insert(temperatures) # Insert integer data only
    # insertion complete

    # >> > tracker.get_max()
    # 31

    # >> > tracker.get_min()
    # 2

    # >> > tracker.get_mean() # Get the average of all recorded data
    # 16.43
    temperatures = [22, 7, 22, 13, 2, 31, 18]
    tracker = TempTracker()
    tracker.insert(temperatures)
    max_value = tracker.get_max()
    min_value = tracker.get_min()
    mean_value = tracker.get_mean()

    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"Mean: {mean_value}")


if __name__ == "__main__":
    runFlatten()
    runTrackers()

