#!/usr/bin/python3


class LockedClass:
    '''define a class that prevents the user from dynamically 
    creating new instance attribute
    '''
    __slots__ = ['last_name']
