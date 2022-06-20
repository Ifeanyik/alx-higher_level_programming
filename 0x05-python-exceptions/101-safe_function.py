def safe_function(fct, *args):
    try:
        global func
        func = fct(*args)
        return func
    except Exception as error:
        print("Exception: {}".format(error))
        return None
