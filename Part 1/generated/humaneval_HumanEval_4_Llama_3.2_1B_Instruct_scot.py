# humaneval_HumanEval_4 | Model: Llama_3.2_1B_Instruct | Strategy: scot
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
    Compute Mean Absolute Deviation around the mean of the given dataset.
    
    Args:
        numbers (List[float]): The input list of numbers.
    
    Returns:
        float: The Mean Absolute Deviation of the input dataset.
    
    Raises:
        ValueError: If the input list is empty.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list must not be empty")
    
    # Compute n = len(numbers)
    n = len(numbers)
    
    # Compute mean = sum(numbers) / n
    mean = sum(numbers) / n
    
    # For each x in numbers, compute abs(x - mean) and accumulate these values
    sum_of_abs_diffs = sum([abs(x - mean) for x in numbers])
    
    # Compute mad = sum_of_abs_diffs / n
    mad = sum_of_abs_diffs / n
    
    return mad
