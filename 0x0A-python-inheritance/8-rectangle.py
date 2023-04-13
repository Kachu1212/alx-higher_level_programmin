#!/usr/bin/python3

"""Define the class Rectangle that inherits from a Base Geometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents the rectangle with Base Geometry."""

    def __init__(self, width, height):
        """Create a new Rectangle.
        Args:
            width (int): width of the new Rectangle.
            height (int): height of the new Rectangle.
        """
        
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
