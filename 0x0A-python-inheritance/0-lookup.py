#!/usr/bin/python3

"""Defines the obj attribute lookup function."""


def lookup(obj):
    """Return the list of an obj attributes."""
    return (dir(obj))
