# humaneval_HumanEval_9 | Model: OLMo_2_1B | Strategy: cot
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
    # Initialize an empty list to store the rolling maximums
    rolling_maxs = []

    # Check if the list is empty
    if not numbers:
        return rolling_maxs  # Return an empty list if the list is empty

    # Find the first number in the list
    num1 = numbers[0]

    # Initialize the current maximum to the first number
    current_max = num1

    # Iterate over the rest of the list
    for num in numbers[1:]:
        # Update the current maximum with the larger number found so far
        current_max = max(current_max, num)

        # Append the current maximum to the rolling maximum list
        rolling_maxs.append(current_max)

    # Return the rolling maximum list
    return rolling_maxs