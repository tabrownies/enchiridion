"""This file runs tests on the time_function function from the timer module. It expects to be used by the pytest library."""
import pytest

from timer import time_function

def test_time_function():
    """Test the time_function function."""
    # Step 1: Define a simple function to time
    def add(a, b):
        return a + b
    
    # Step 2: Time the function
    execution_time, value = time_function(add, 1, 2)
    
    # Step 3: Check the execution time
    assert execution_time > 0
    
    # Step 4: Check the return value
    assert value == 3

# Run the tests if this file is executed
if __name__ == "__main__":
    pytest.main(["-v", __file__])