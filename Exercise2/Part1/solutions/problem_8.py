from typing import List, Tuple
    import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.

    Args:
        numbers: A list of integers.

    Returns:
        A tuple containing the sum and product of all integers in the list.
    """

    # First, compute the sum of all numbers in the list.
    # The built-in sum() function works with lists and returns the sum of its elements.
    # We use a conditional expression to ensure the sum is 0 when the list is empty.
    total_sum = sum(numbers or [0]) if numbers else 0

    # Next, compute the product of all numbers in the list.
    # We initialize the product as 1 and then multiply it by each number in the list.
    # We use the math.prod() function if available (Python 3.8+).
    # Otherwise, we use a loop.
    total_product = math.prod(numbers or [1]) if numbers else 1

    # Finally, return a tuple containing the sum and product.
    return total_sum, total_product
