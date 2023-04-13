#!/usr/bin/python3

"""Define the function that adds attributes with objects."""


def add_attribute(obj, att, value):
    """Add the new attribute to an object if feasible.
    Args:
        obj (any): object to add an attribute to.
        att (str): name of the attribute to add to obj.
        value (any): value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
