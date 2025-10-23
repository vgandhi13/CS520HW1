# humaneval_HumanEval_0 | Model: OLMo_2_1B | Strategy: cot
# Entry point: has_close_elements

# Problem prompt:
# from typing import List
# 
# 
# def has_close_elements(numbers: List[float], threshold: float) -> bool:
#     """ Check if in given list of numbers, are any two numbers closer to each other than
#     given threshold.
#     >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
#     False
#     >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
#     True
#     """
# 

# Paste your generated code below

import numpy as np

def has_close_elements(numbers, threshold):
    """
    Checks if any two numbers in the given list are closer than a specified threshold.
    """
    
    # Check if the list is empty
    if not numbers:
        return True  # True because an empty list has at least one pair of equal elements
    
    # Sort the list
    numbers.sort()
    
    # Iterate through the sorted list and check the condition
    for i in range(len(numbers) - 1):
        if np.abs(numbers[i] - numbers[i+1]) < threshold:
            return True
    
    # If no such pair is found after checking all pairs, return False
    return False