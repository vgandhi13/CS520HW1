# humaneval_HumanEval_5 | Model: Llama_3.2_1B_Instruct | Strategy: cot
# Entry point: intersperse

# Problem prompt:
# from typing import List
# 
# 
# def intersperse(numbers: List[int], delimeter: int) -> List[int]:
#     """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
#     >>> intersperse([], 4)
#     []
#     >>> intersperse([1, 2, 3], 4)
#     [1, 4, 2, 4, 3]
#     """
# 

# Paste your generated code below

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
        # Append the current element
        result.append(num)
        # If we're not at the last element, append the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)
    
    return result