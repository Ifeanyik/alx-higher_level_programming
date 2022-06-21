#!/usr/bin/python3
def safe_function(fct, *args):
    func = None
    try:
        func = fct(*args)
        return func
    except Exception as error:
        try:
            print("Exception: {}".format(error))
            return None
        except Exception as err:
            print("Exception: {}".format(err))
            return None
