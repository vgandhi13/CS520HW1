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
