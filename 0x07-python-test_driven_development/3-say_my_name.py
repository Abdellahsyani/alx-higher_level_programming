#!/usr/bin/python3
'''Define a function to print names'''


def say_my_name(first_name, last_name=""):
    '''print first name and last name

    Args:
        say_my_name(list): print name
        first_name: the name
        last_name: the name
        Return: the names
    Raises:
        TypeError: if first_name not string
        TypeError: if first_name not string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
