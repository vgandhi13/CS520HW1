# humaneval_HumanEval_2 | Model: Llama_3.2_1B_Instruct | Strategy: cot
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
def truncate_number(number):
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    
    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Calculate the decimal part by subtracting the integer part from the original number
    decimal_part = number - math.floor(number)
    
    # Return the decimal part
    return decimal_part