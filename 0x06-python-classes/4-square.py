#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def area(self):
        """Return the current area of the square."""
        return (self.size * self.size)
