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
