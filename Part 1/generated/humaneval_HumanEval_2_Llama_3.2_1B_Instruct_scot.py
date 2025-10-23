# humaneval_HumanEval_2 | Model: Llama_3.2_1B_Instruct | Strategy: scot
# Entry point: truncate_number

# Problem prompt:
# 
# 
# def truncate_number(number: float) -> float:
#     """ Given a positive floating point number, it can be decomposed into
#     and integer part (largest integer smaller than given number) and decimals
#     (leftover part always smaller than 1).
# 
#     Return the decimal part of the number.
#     >>> truncate_number(3.5)
#     0.5
#     """
# 

# Paste your generated code below

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

# Test cases
print(truncate_number(3.5))   # Expected output: 0.5
print(truncate_number(5.0))   # Expected output: 0.0
print(truncate_number(0.75)) # Expected output: 0.75