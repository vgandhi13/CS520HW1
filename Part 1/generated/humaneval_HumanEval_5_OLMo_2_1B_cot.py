# humaneval_HumanEval_5 | Model: OLMo_2_1B | Strategy: cot
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

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        result.append(delimeter)
    return result