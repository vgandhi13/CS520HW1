# humaneval_HumanEval_3 | Model: Llama_3.2_1B_Instruct | Strategy: cot
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
    balance = 0  # Initialize the balance to 0
    
    for operation in operations:
        balance += operation  # Update the balance for each operation
        if balance < 0:  # Check if the balance is negative
            return True  # If the balance is negative, return True
    
    return False  # If no negative balance is found, return False
