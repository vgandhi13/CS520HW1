# humaneval_HumanEval_8 | Model: OLMo_2_1B | Strategy: cot
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

# Function to compute the sum and product of a list of integers
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # Compute the sum
    total_sum = sum(numbers)

    # Initialize the product to 1 (or math.prod() for Python 3.8+ which provides a more efficient way)
    product = 1

    # Iterate over the list
    for num in numbers:
        # Update product
        product *= num

    # Return the sum and product
    return (total_sum, product)