#!/usr/bin/python3
""" Defines a function that returns True if the object is an instance of"""


def inherits_from(obj, a_class):
    """
    returns True if the object is
    and instance of a class that inherited from
    the specified class; otherwise False
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
