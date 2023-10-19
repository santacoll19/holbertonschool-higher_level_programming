#!/usr/bin/python3
""" function that returns True if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """True if the object is exactly an instance of the specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
