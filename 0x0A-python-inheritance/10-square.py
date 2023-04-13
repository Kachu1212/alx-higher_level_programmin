#!/usr/bin/python3

"""Define the Rectangle sub-class Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents the square."""

    def __init__(self, size):
        """creates new square.
        Args:
            size (int): size of the new square.
        """
        
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
