#!/usr/bin/python3
if __name__ == "__main__":
    '''calculator'''
    import sys
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)
    elif op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)
    sys.exit(0)
