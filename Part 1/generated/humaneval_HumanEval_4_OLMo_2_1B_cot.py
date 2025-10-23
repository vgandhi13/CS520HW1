# humaneval_HumanEval_4 | Model: OLMo_2_1B | Strategy: cot
# Entry point: mean_absolute_deviation

# Problem prompt:
# from typing import List
# 
# 
# def mean_absolute_deviation(numbers: List[float]) -> float:
#     """ For a given list of input numbers, calculate Mean Absolute Deviation
#     around the mean of this dataset.
#     Mean Absolute Deviation is the average absolute difference between each
#     element and a centerpoint (mean in this case):
#     MAD = average | x - x_mean |
#     >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
#     1.0
#     """
# 

# Paste your generated code below
from typing import List
import math


def mean_absolute_deviation(numbers: List[float]) -> float:

# Step-by-step explanation:

# * Define the function mean_absolute_deviation
# * Accept a list of floats as input
# * Calculate the mean of the numbers in the list
    mean = sum(numbers) / len(numbers)
    
    # Initialize the absolute deviation list
    abs_diff = [abs(x - mean) for x in numbers]

# * Compute the mean absolute deviation (MAD)
    mad = sum(abs_diff) / len(numbers)

# * Handle edge case: if the list is empty, return 0 due to division by zero
    if len(numbers) == 0:
        return 0.0

# * Ensure the list doesn't contain zero to avoid division by zero
    for num in numbers:
        if num == 0:
            raise ValueError("List must not contain zero.")

    # * Print the result
    return mean
