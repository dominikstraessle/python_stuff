# https://www.python.org/dev/peps/pep-0343/
class ContextManager:
    def __init__(self) -> None:
        # 1. Init required variables
        pass

    def __enter__(self) -> object:
        # 1. Create and return the required object
        return object
        pass

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        # 1. Handle Exceptions
        # 2. Close IO, Connections etc...
        pass
