# humaneval_HumanEval_8 | Model: OLMo_2_1B | Strategy: scot
# Entry point: sum_product

# Problem prompt:
# from typing import List, Tuple
# 
# 
# def sum_product(numbers: List[int]) -> Tuple[int, int]:
#     """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
#     Empty sum should be equal to 0 and empty product should be equal to 1.
#     >>> sum_product([])
#     (0, 1)
#     >>> sum_product([1, 2, 3, 4])
#     (10, 24)
#     """
# 

# Paste your generated code below
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list."""
    
    # Initialize total sum and product to 0 and 1 respectively
    total_sum = 0
    total_product = 1
    
    # Iterate through each element in the list
    for n in numbers:
        # Add the current number to the total sum
        total_sum += n
        
        # Multiply the total product by the current number
        total_product *= n
    
    # Return a tuple with the sum and product
    return (total_sum, total_product)