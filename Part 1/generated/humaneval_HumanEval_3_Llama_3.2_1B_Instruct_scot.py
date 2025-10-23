# humaneval_HumanEval_3 | Model: Llama_3.2_1B_Instruct | Strategy: scot
# Entry point: below_zero

# Problem prompt:
# from typing import List
# 
# 
# def below_zero(operations: List[int]) -> bool:
#     """ You're given a list of deposit and withdrawal operations on a bank account that starts with
#     zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
#     at that point function should return True. Otherwise it should return False.
#     >>> below_zero([1, 2, 3])
#     False
#     >>> below_zero([1, 2, -4, 5])
#     True
#     """
# 

# Paste your generated code below

from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    Detect if at any point the balance of account falls below zero.

    Args:
        operations (List[int]): A list of deposit and withdrawal operations.

    Returns:
        bool: True if the balance falls below zero at any point, False otherwise.
    """
    balance = 0  # Initialize balance to 0
    
    # Iterate through each operation in the list
    for op in operations:
        balance += op  # Update the balance
        
        # Check if balance is less than 0
        if balance < 0:
            return True  # Return True if balance is less than 0
    
    # If the loop completes and balance never went below zero
    return False  # Return False