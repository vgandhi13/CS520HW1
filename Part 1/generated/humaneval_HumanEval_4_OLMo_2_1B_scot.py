# humaneval_HumanEval_4 | Model: OLMo_2_1B | Strategy: scot
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

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculates the Mean Absolute Deviation of a set of numbers.
    
    Args:
    - numbers: A list of floats.

    Returns:
    - The Mean Absolute Deviation (MAD) of the input numbers.
    """
    # Check if input is a list of floats
    if not isinstance(numbers, list) or not all(isinstance(x, float) for x in numbers):
        raise ValueError("Input must be a list of floats.")

    # Calculate the mean
    mean = sum(numbers) / len(numbers)

    # Compute the absolute differences from the mean and sum them up
    abs_diffs = [abs(x - mean) for x in numbers]
    total_abs_diffs = sum(abs_diffs)

    # Calculate the mean absolute deviation
    mad = total_abs_diffs / len(numbers)

    return mad