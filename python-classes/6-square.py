#!/usr/bin/python3
""" This is a empty file """


class Square():
    """Empty class"""

    def __init__(self, size=0, position=(0, 0)):
        """ constructor method """
        self.__size = size
        self.position = position
        
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Getter method for position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Setter method for size"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
            
    def area(self):
        """return the square area"""
        return (self.__size)**2

    def my_print(self):
        """ Print a square of size size"""
        if (self.__size == 0):
            print("")
            return
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
