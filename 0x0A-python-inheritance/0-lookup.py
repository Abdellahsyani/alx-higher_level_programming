#!/usr/bin/python3
'''Define an attribute lookup function'''


def lookup(obj):
    '''the function started'''
    return (dir(obj))


class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
