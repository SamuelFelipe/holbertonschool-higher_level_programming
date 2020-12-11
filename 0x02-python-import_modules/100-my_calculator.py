#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, mul, div, sub

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    sig = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if sig == '+':
        print("{} {} {} = {}".format(a, sig, b, add(a, b)))
    elif sig == '-':
        print("{} {} {} = {}".format(a, sig, b, sub(a, b)))
    elif sig == '*':
        print("{} {} {} = {}".format(a, sig, b, mul(a, b)))
    elif sig == '/':
        print("{} {} {} = {}".format(a, sig, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
