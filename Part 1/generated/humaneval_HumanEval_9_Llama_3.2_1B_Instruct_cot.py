# humaneval_HumanEval_9 | Model: Llama_3.2_1B_Instruct | Strategy: cot
# Entry point: rolling_max

# Problem prompt:
# from typing import List, Tuple
# 
# 
# def rolling_max(numbers: List[int]) -> List[int]:
#     """ From a given list of integers, generate a list of rolling maximum element found until given moment
#     in the sequence.
#     >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
#     [1, 2, 3, 3, 3, 4, 4]
#     """
# 

# Paste your generated code below
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:  # edge case: empty list
        return []
    
    current_max = float('-inf')  # initialize current_max to negative infinity
    result = []  # initialize result list
    
    for num in numbers:
        # update current_max if the number is larger
        current_max = max(current_max, num)
        # append the current maximum to the result list
        result.append(current_max)
    
    return result