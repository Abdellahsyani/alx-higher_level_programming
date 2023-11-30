#!/usr/bin/python3
'''authur abdellah syani (())'''

if __name__ == "__main__":
    '''the function to print all hidden names'''
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if  not name.startswitch("__"):
            print(name)
