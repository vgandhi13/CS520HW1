def truncate_number(number):
    """
    Given a positive floating-point number, it can be decomposed into
    its integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Return the decimal part of the number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    # Get the integer part of the number
    integer_part = int(number)
    
    # Get the decimal part by subtracting the integer part from the original number
    decimal_part = number - integer_part
    
    return decimal_part
