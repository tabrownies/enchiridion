"""This file runs tests on the time_function function from the timer module. It expects to be used by the command python3 -m pytest --cov"""
import time

from timer import time_function

def test_time_function():
    """Test the time_function function."""
    # Step 1: Define a simple function to time and values to be used with it
    def add(a, b):
        return a + b
    
    a = 1
    b = 2
    
    # Step 2: Time the function
    execution_time, value = time_function(add, a, b)

    # Step 3: Check that the execution time is postive
    assert execution_time > 0
    
    # Step 4: Find the execution time with the time library and compare the two. The difference should be within 0.1 seconds.
    start_time = time.time()
    expected_value = add(a, b)
    end_time = time.time()
    expected_execution_time = end_time - start_time
    assert abs(execution_time - expected_execution_time) < 0.1 # this difference is arbitrary
    
    # Step 5: Check the return value
    assert value == expected_value
