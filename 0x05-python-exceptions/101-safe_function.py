#!/usr/bin/python3
def safe_function(fct, *args):
    func = None
    try:
        func = fct(*args)
        return func
    except Exception as error:
        print("Exception: {}".format(error))
        return None
