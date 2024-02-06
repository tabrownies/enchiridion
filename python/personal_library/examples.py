# This file contains examples of using different loading symbols for a loading animation.
# It demonstrates the usage of a list, a function, and an object to generate loading symbols.
# The examples are executed in a loop with a delay of 0.3 seconds between each iteration.
# The purpose of this file is to showcase different approaches to creating loading animations using the custom library.

import time
from loading import loading_dots_function
from loading_symbols import loading_spinner_symbols

# Example 1: Using a list imported from loading_symbols.py
loading_symbols = loading_spinner_symbols
list_func = loading_dots_function(loading_symbols)

# Example 2: Using a function
def custom_loading_symbols(index):
    """
    Custom loading symbols function.
    
    Args:
        index (int): The index of the loading symbol.
    
    Returns:
        str: The loading symbol corresponding to the index.
    """
    if index % 4 == 0:
        return '-'
    elif index % 4 == 1:
        return '+'
    elif index % 4 == 2:
        return '*'
    else:
        return '/'

func_func = loading_dots_function(custom_loading_symbols)

# Example 3: Using an object
class LoadingSymbols:
    """
    LoadingSymbols class.
    """
    def __init__(self):
        self.symbols = ['.  ', '..  ', '...']
        
    def __getitem__(self, index):
        """
        Get the loading symbol at the given index.
        
        Args:
            index (int): The index of the loading symbol.
        
        Returns:
            str: The loading symbol corresponding to the index.
        """
        return self.symbols[index%len(self.symbols)]

loading_symbols_object = LoadingSymbols()
obj_func = loading_dots_function(loading_symbols_object)

# Loop through the examples and print the loading symbols
for i in range(20):    
    print(f'{list_func(i)} {func_func(i)} {obj_func(i)}', end='\r')
    time.sleep(0.3)