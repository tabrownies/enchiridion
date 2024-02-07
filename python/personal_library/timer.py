"""This file contains a function that takes other functions and times them. It is used to compare the performance of different functions."""
import time

def time_function(func, *args, **kwargs):
    """
    Time the execution of a function and return the execution time and the return value.
    
    Args:
        func (function): The function to time.
        *args: The positional arguments to pass to the function.
        **kwargs: The keyword arguments to pass to the function.
    
    Returns:
        tuple: A tuple containing the execution time (in seconds) and the return value of the function.
    """
    # Step 1: Record the start time
    start_time = time.time()
    
    # Step 2: Execute the function with the provided arguments
    value = func(*args, **kwargs)
    
    # Step 3: Record the end time
    end_time = time.time()
    
    # Step 4: Calculate the execution time
    execution_time = end_time - start_time
    
    # Step 5: Return the execution time and the return value as a tuple
    return execution_time, value
