from functools import wraps

def decorator_name(func):
    """This is a template for creating a decorator function in python[1].
        [1]: https://www.oreilly.de/buecher/12789/9783960090359-python-von-kopf-bis-fu%C3%9F.html"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Before Calling the decorated function

        # 2. Call the decorated function as required,
        #    returning its results if needed.
        return func(*args, **kwargs)

        # 3. Code to execute instead of calling the decorated function.
    return wrapper
