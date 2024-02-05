# This file is used to test the loading.py file
from loading import loading_dots_function
from loading_symbols import loading_armenian_alphabet_lowercase

def test_loading_dots_function():
    # test loading_dots_function with a list and a index within the lists range
    assert loading_dots_function(loading_symbols=loading_armenian_alphabet_lowercase, raise_errors=False)(0) == loading_armenian_alphabet_lowercase[0]
    # test loading_dots_function with a list and a index outside the lists range
    assert loading_dots_function(loading_symbols=loading_armenian_alphabet_lowercase, raise_errors=False)(39) == loading_armenian_alphabet_lowercase[39%len(loading_armenian_alphabet_lowercase)]
    # test loading_dots_function with a function that takes in an index and outputs a string
    assert loading_dots_function(loading_symbols=lambda index: 'a', raise_errors=False)(0) == 'a'
    # test loading_dots_function with a function that takes in no valuables and outputs a string
    assert loading_dots_function(loading_symbols=lambda: 'a', raise_errors=False)(0) == '[\\]'
    # test loading_dots_function with a object that has a __getitem__ method
    class TestObject:
        def __getitem__(self, index):
            return 'a'
    assert loading_dots_function(loading_symbols=TestObject(), raise_errors=False)(0) == 'a'    