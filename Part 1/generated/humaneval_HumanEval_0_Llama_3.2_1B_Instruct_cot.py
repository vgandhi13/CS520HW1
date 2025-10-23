# humaneval_HumanEval_0 | Model: Llama_3.2_1B_Instruct | Strategy: cot
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
from typing import List
def has_close_elements(numbers: list[float], threshold: float) -> bool:
    """
    Check if any two numbers in a list are closer to each other than a given threshold.

    Args:
    numbers (list[float]): The list of numbers to check.
    threshold (float): The threshold value.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Check for edge cases
    if len(numbers) < 2:
        # If the list has less than 2 numbers, we can't find a pair
        return False

    # Sort the list of numbers
    # This operation has a time complexity of O(n log n)
    numbers.sort()

    # Iterate over the sorted list and compare adjacent numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        difference = numbers[i + 1] - numbers[i]

        # If the difference is less than the threshold, we have found a pair
        if difference < threshold:
            return True

    # If we haven't found a pair, return False
    return False
