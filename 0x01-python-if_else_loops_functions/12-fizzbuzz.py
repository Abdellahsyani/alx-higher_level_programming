#!/usr/bin/python3
#Authur abdellah#

def fizzbuzz():
    for i in range(1, 101):
        if (i % 3) == 0:
            print("Fizz")
        elif (i % 5) == 0:
            print("Buzz")
        elif (i % 3 and i % 5) == 0:
            print("FizzBuzz")