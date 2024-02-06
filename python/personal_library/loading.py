"""This file contains functions to create loading symbols"""

from loading_symbols import loading_spinner_symbols

def loading_dots_function(loading_symbols, raise_errors=True):
    """
    Returns a function that can be called to create loading symbols
    
    Parameters:
    loading_symbols (list, or function(index)->string, object): If a list, use those symbols as the loading symbols, if a function then use it as a callback to get the loading symbol at the given index. If an object, check for the __getitem__ method and use it as a callback to get the loading symbol at the given index.
    raise_errors (bool): If True, raise an error if the loading_symbols is not a list, a function, or an object with an __getitem__ method. If False, return a loading spinner symbols.
    Returns:
    function(index)->string: A function that takes an index and returns the corresponding loading symbol.
    """
    def handle_error(error_message):
        if raise_errors:
            raise ValueError(error_message)
        else:
            return lambda index: loading_spinner_symbols[index%len(loading_spinner_symbols)]

    # check if the loading_symbols is a list and return the corresponding loading function
    if type(loading_symbols) == list:
        return lambda index: str(loading_symbols[index%len(loading_symbols)])
    # check if the loading_symbols is a function, verify it takes an index, and return it
    elif callable(loading_symbols):
        # verify it takes a single parameter or has only one non-default parameter
        if len(loading_symbols.__code__.co_varnames) == 1:
            return loading_symbols
        else:
            # properly handle the error
            try:
                return handle_error('The loading_symbols function must take a single parameter') 
            # propagate it up
            except ValueError as e:
                raise e
    # check if the loading_symbols is an object, verify it has an __getitem__ method, and return it
    elif hasattr(loading_symbols, '__getitem__'):
        return loading_symbols.__getitem__
    else:
        # properly handle the error
        try:
            return handle_error('The loading_symbols must be a list, a function, or an object with an __getitem__ method')
        # propagate it up
        except ValueError as e:
            raise e