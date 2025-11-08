import math

def truncate_number(number):
    """
    Given a positive floating point number, it can be decomposed into 
    integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    """
    
    # Compute the integer part using math.floor function
    integer_part = math.floor(number)
    
    # Subtract this integer part from the original number to isolate the decimal part
    decimal_part = number - integer_part
    
    # Return the result
    return decimal_part
