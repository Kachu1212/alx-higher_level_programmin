#!/usr/bin/python3

"""Defines the inherited class called MyList."""


class MyList(list):
    """Implements a sorted printing exec for built-in list class."""

    def print_sorted(self):
        """Prints the list in sorted ascending manner."""
        print(sorted(self))
