#!/usr/bin/python3

"""Defines the function for checking class."""


def is_same_class(obj, a_class):
    """Checks if the bject is an accurate instance of ant given class.
    Args:
        obj (any): The object to be checked.
        a_class (type): The class that must match the type of obj.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    
    if type(obj) == a_class:
        return True
    return False
