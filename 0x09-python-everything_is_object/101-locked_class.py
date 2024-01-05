#!/usr/bin/python3
'''define'''


class LockedClass:
    '''define a class that prevents the user from dynamically 
    creating new instance attribute
    '''
    __slots__ = ["first_name"]
