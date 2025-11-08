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
