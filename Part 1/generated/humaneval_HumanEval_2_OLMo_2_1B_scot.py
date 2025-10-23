# humaneval_HumanEval_2 | Model: OLMo_2_1B | Strategy: scot
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

from math import floor
def truncate_number(number):
    # Get the integer part using floor
    int_part = floor(number)
    
    # Get the decimal part
    decimal_part = number - int_part

    return int_part, decimal_part
