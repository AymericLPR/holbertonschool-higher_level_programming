#!/usr/bin/python3
""" This is a file of a empty class square """


class Square:
    """Empty class"""
    def __init__(self, size=0):
        """initialisation of values"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """ Return square area """
            return self.__size * self.__size
