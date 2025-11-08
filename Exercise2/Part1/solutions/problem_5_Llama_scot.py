from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): Input list of integers
    delimeter (int): Number to insert between elements
    
    Returns:
    List[int]: List with delimeter inserted between every two consecutive elements
    """
    
    # If numbers is empty or has only one element, return numbers as is
    if len(numbers) < 2:
        return numbers
    
    # Initialize an empty list result
    result = []
    
    # Iterate through the list using index i
    for i in range(len(numbers)):
        # If i is not the last index, append the delimeter to result
        if i != len(numbers) - 1:
            result.append(delimeter)

        # Append numbers[i] to result
        result.append(numbers[i])

    # Return result
    return result
