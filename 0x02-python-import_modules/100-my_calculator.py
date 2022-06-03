#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    call = sys.argv
    if len(call) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(call[1])
    b = int(call[3])
    if call[2] == "+":
        print("{} {} {} = {}".format(a, call[2], b, calc.add(a, b)))
    elif call[2] == "-":
        print("{} {} {} = {}".format(a, call[2], b, calc.sub(a, b)))
    elif call[2] == "*":
        print("{} {} {} = {}".format(a, call[2], b, calc.mul(a, b)))
    elif call[2] == "/":
        print("{} {} {} = {}".format(a, call[2], b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
