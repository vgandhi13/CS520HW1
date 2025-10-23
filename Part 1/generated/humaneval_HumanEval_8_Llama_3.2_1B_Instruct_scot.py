# humaneval_HumanEval_8 | Model: Llama_3.2_1B_Instruct | Strategy: scot
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
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    """
    
    # Initialize total_sum and total_product
    total_sum = 0
    total_product = 1
    
    # Iterate through each element n in numbers
    for n in numbers:
        # Add n to total_sum
        total_sum += n
        
        # Multiply total_product by n
        total_product *= n
    
    # Return (total_sum, total_product)
    return total_sum, total_product