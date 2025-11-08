from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum element found until given moment.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of rolling maximum elements.
    """
    
    # Initialize result as an empty list and current_max as the first number in the list
    result = []
    current_max = numbers[0]
    # Initialize window size as 0
    window_size = 0
    
    # Open parenthesis to square brackets is placed to display math notation
    for n in numbers:
        # If the current number is greater than the current maximum, update current_max
        if n > current_max:
            current_max = n
        
        # If the window size is larger than one, remove elements from the start of the result
        if window_size > 1:
            result.append(current_max)
            # Decrease the window size by one
            window_size -= 1
        
        # If the window size is one, append the current number to the result and increment the window size
        if window_size == 1:
            result.append(n)
            window_size = 1

    return result
