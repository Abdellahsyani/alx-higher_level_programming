#!/usr/bin/python3
'''Define a class that do something'''


class MyList(list):
    '''start a class'''
    def __init__(self):
        '''the init method'''
        supper().__init__()

    def print_sorted(self):
        '''sorted function'''
        print(sorted(self))
