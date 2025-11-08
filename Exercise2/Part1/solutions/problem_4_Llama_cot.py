from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Compute the Mean Absolute Deviation (MAD) of a list of numbers.

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        float: The Mean Absolute Deviation (MAD) of the input list.

    Raises:
        ValueError: If the input list is empty.

    """
    # Step 1: Calculate the sum of all numbers
    total_sum = sum(numbers)

    # Step 2: Check if the list is empty
    if len(numbers) == 0:
        # Return the MAD of an empty list is undefined, raise a ValueError instead
        raise ValueError("Cannot compute MAD of an empty list")

    # Step 3: Calculate the mean of the list
    mean = total_sum / len(numbers)

    # Step 4: Compute the absolute difference between each number and the mean, sum them up
    abs_diff = [abs(x - mean) for x in numbers]

    # Step 5: Calculate the mean of the absolute differences
    mad = sum(abs_diff) / len(numbers)

    return mad
