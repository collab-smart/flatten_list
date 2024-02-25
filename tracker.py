#!/usr/bin/python
"""tracker.py - Tracker classes file
"""
from statistics import mean


class GenericTracker:
    """A class used to represent a Generic Tracker

    Attributes:
        items (list): The recorded data list of tracker.

    Methods:
        insert(items): Insert data list into a tracker.
        get_mean(): Get the average of recorded data in a tracker.
    """
    def __init__(self):
        self.items = []

    def insert(self, items):
        """Insert item list (integer data only).

        Args:
            items (list): Tracker data list - integers only.

        Returns:
            list: A list of recorded data on tracker.
        """
        self.items = [item for item in items if isinstance(item, int)]
        print("Insertion complete")
        return self.items

    def get_mean(self):
        """ Get the average of all items with the precision upto 2 decimal value."""
        return round(mean(self.items), 2) if self.items else 0


class TempTracker(GenericTracker):
    """A class used to represent a Temperature Tracker, a child class of GenericTracker."""

    def get_max(self):
        """Get the maximum value from the recorded data list."""
        return max(self.items)

    def get_min(self):
        """Get the minimum value from the recorded data list."""
        return min(self.items)


