from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a delimiter between every two consecutive elements in the input list.

    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The delimiter to insert between elements.

    Returns:
        List[int]: The modified list with delimiters inserted.
    """
    
    # Handle edge case where input list is empty
    if not numbers:
        return []
    
    # Handle edge case where input list has only one element
    if len(numbers) == 1:
        return numbers
    
    # Initialize a new list to store the modified elements
    result = []
    
    # Iterate through the input list, adding elements to the result list
    for i, num in enumerate(numbers):
        # If we're not at the last element, append the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)
        # Append the current element
        result.append(num)
    
    return result
