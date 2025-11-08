from typing import List, Tuple

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
