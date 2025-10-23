# humaneval_HumanEval_9 | Model: OLMo_2_1B | Strategy: scot
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
    if not numbers:
        return []
    
    result = []
    current_max = numbers[0]
    
    for n in numbers:
        if n > current_max:
            current_max = n
        else:
            result.append(current_max)
    
    return result