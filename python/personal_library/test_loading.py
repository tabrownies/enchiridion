# This file is used to test the loading.py file
from loading import loading_dots_function
from loading_symbols import loading_armenian_alphabet_lowercase

def test_loading_dots_function():
    # test loading_dots_function with a list and a index within the lists range and avoiding raising errors
    assert loading_dots_function(loading_symbols=loading_armenian_alphabet_lowercase, raise_errors=False)(0) == loading_armenian_alphabet_lowercase[0]
    # test loading_dots_function with a list and a index outside the lists range and avoiding raising errors
    assert loading_dots_function(loading_symbols=loading_armenian_alphabet_lowercase, raise_errors=False)(39) == loading_armenian_alphabet_lowercase[39%len(loading_armenian_alphabet_lowercase)]
    # test loading_dots_function with a function that takes in an index and outputs a string and avoiding raising errors
    assert loading_dots_function(loading_symbols=lambda index: 'a', raise_errors=False)(0) == 'a'
    # test loading_dots_function with a function that takes in no valuables and outputs a string and avoiding raising errors
    assert loading_dots_function(loading_symbols=lambda: 'a', raise_errors=False)(0) == '[\\]'
    # test loading_dots_function with a object that has a __getitem__ method and avoiding raising errors
    class TestObject:
        def __getitem__(self, index):
            return 'a'
    assert loading_dots_function(loading_symbols=TestObject(), raise_errors=False)(0) == 'a'   
    # test loading_dots_function with an incorrect input and a index within the lists range and raising errors 
    try:
        loading_dots_function(loading_symbols=1)(0)
    except ValueError as e:
        assert str(e) == 'The loading_symbols must be a list, a function, or an object with an __getitem__ method'
    # test loading_dots_function with an incorrect function and raising errors
    try:
        loading_dots_function(loading_symbols=lambda: 'a')(0)
    except ValueError as e:
        assert str(e) == 'The loading_symbols function must take a single parameter'