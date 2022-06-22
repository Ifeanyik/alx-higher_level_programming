#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    func = None
    try:
        func = fct(*args)
        return func
    except Exception as error:
        try:
            print("Exception: {}".format(error), file=stderr)
            return None
        except Exception as err:
            print("Exception: {}".format(err), file=stderr)
            return None
