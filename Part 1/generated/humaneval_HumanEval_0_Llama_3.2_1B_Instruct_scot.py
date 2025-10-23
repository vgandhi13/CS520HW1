# humaneval_HumanEval_0 | Model: Llama_3.2_1B_Instruct | Strategy: scot
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
from typing import List, Tuple

def has_close_elements(numbers: list[float], threshold: float) -> bool:
    """
    Check if any two numbers in the list are closer than the given threshold.

    Args:
        numbers (list[float]): A list of floating point numbers.
        threshold (float): The maximum difference between two numbers to be considered close.

    Returns:
        bool: True if any two numbers are close, False otherwise.
    """
    # Check if the list has fewer than 2 elements and return False if true
    if len(numbers) < 2:
        return False

    # Sort the list in ascending order
    numbers.sort()

    # Iterate through the list with two nested loops
    for i in range(len(numbers) - 1):
        # Compute the absolute difference between each pair of adjacent numbers
        for j in range(i + 1, len(numbers)):
            # Check if the difference is less than the threshold and return True
            if abs(numbers[i] - numbers[j]) < threshold:
                return True

    # If the loop completes without finding a pair closer than the threshold, return False
    return False