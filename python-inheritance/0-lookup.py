#!/usr/bin/python3
"""
function that returns the list of available attributes and methods of an object
"""


def lookup(obj):

    """
    function that returns the list of available 
    attributes and methods of an object
    obj: inspect inside the object
    """

    return dir(obj)
