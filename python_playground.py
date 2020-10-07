





import functools
def compose(*functions):
    """
    Returns 
    """
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)











if __name__ == "__main__":
    pass
    
    
    
    



# generate_closure: given f(*kwargs), create g(*kwargs) where g generates a closure for f based on what args were supplied
# generating contexts: exec_with_context(f, context), where context is a dict of kwargs
# inspect.getsource(function)
# memoizing
###
# functools
# itertools
###
# code from scratch.py
# code from records 





















