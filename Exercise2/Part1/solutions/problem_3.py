from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0  # Initialize the balance to 0
    
    for operation in operations:
        balance += operation  # Update the balance for each operation
        if balance < 0:  # Check if the balance is negative
            return True  # If the balance is negative, return True
    
    return False  # If no negative balance is found, return False
